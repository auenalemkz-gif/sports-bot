import asyncio
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional
import feedparser
import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class NewsFetcher:
    def __init__(self, feeds):
        self.feeds = feeds

    async def get_fresh_articles(self):
        all_articles = []
        async with httpx.AsyncClient(timeout=15, follow_redirects=True) as client:
            tasks = [self._fetch_feed(client, feed) for feed in self.feeds]
            results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, list):
                all_articles.extend(result)
        all_articles.sort(key=lambda x: x.get("published", datetime.min), reverse=True)
        return all_articles

    async def _fetch_feed(self, client, feed_config):
        articles = []
        try:
            response = await client.get(feed_config["url"], headers={"User-Agent": "Mozilla/5.0"})
            feed = feedparser.parse(response.text)
            cutoff = datetime.now(timezone.utc) - timedelta(hours=48)
            for entry in feed.entries[:20]:
                image_url = self._extract_image(entry)
                articles.append({
                    "title": entry.get("title", ""),
                    "summary": entry.get("summary", ""),
                    "url": entry.get("link", ""),
                    "image_url": image_url,
                    "sport": feed_config["sport"],
                    "lang": feed_config.get("lang", "ru"),
                    "published": datetime.now(timezone.utc),
                    "source": feed.feed.get("title", feed_config["url"]),
                })
        except Exception as e:
            logger.warning(f"Ошибка: {e}")
        return articles

    def _extract_image(self, entry):
        if hasattr(entry, "media_content") and entry.media_content:
            for m in entry.media_content:
                if m.get("url"):
                    return m["url"]
        if hasattr(entry, "media_thumbnail") and entry.media_thumbnail:
            return entry.media_thumbnail[0].get("url")
        summary = entry.get("summary", "")
        if summary:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(summary, "html.parser")
            img = soup.find("img")
            if img and img.get("src"):
                return img["src"]
        return None
