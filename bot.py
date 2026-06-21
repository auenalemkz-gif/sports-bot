import asyncio
import logging
import random
from telegram import Bot
from telegram.error import TelegramError
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID, ANTHROPIC_API_KEY, POSTS_PER_DAY, RSS_FEEDS
from news_fetcher import NewsFetcher
from content_generator import ContentGenerator
from storage import PostedStorage

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

class SportNewsBot:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
        self.fetcher = NewsFetcher(RSS_FEEDS)
        self.generator = ContentGenerator(ANTHROPIC_API_KEY)
        self.storage = PostedStorage()
        self.scheduler = AsyncIOScheduler()

    async def post_news(self):
        try:
            articles = await self.fetcher.get_fresh_articles()
            if not articles:
                return
            new_articles = [a for a in articles if not self.storage.is_posted(a["url"])]
            if not new_articles:
                return
            article = random.choice(new_articles[:10])
            post_text = await self.generator.generate_post(article)
            image_url = article.get("image_url")
            try:
                if image_url:
                    await self.bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=image_url, caption=post_text, parse_mode="HTML")
                else:
                    await self.bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=post_text, parse_mode="HTML")
            except TelegramError:
                await self.bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=post_text, parse_mode="HTML")
            self.storage.mark_posted(article["url"])
            logger.info(f"Опубликовано: {article['title'][:60]}")
        except Exception as e:
            logger.error(f"Ошибка: {e}")

    def setup_scheduler(self):
        start_hour = 8
        end_hour = 23
        interval = ((end_hour - start_hour) * 60) // POSTS_PER_DAY
        for i in range(POSTS_PER_DAY):
            minute_offset = i * interval + random.randint(0, 10)
            hour = start_hour + minute_offset // 60
            minute = minute_offset % 60
            if hour < end_hour:
                self.scheduler.add_job(self.post_news, "cron", hour=hour, minute=minute)

    async def run(self):
        logger.info("Запуск Sports News Bot...")
        me = await self.bot.get_me()
        logger.info(f"Бот подключён: @{me.username}")
        self.setup_scheduler()
        self.scheduler.start()
        await self.post_news()
        while True:
            await asyncio.sleep(60)

if __name__ == "__main__":
    bot = SportNewsBot()
    asyncio.run(bot.run())
