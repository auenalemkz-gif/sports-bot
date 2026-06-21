import logging
import httpx
from config import SYSTEM_PROMPT, MAX_CAPTION_LENGTH

logger = logging.getLogger(__name__)

class ContentGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.anthropic.com/v1/messages"

    async def generate_post(self, article):
        if not self.api_key:
            return self._fallback_format(article)
        has_photo = bool(article.get("image_url"))
        user_prompt = f"""Напиши пост для Telegram на русском языке.
Заголовок: {article['title']}
Описание: {article.get('summary', '')[:300]}
Вид спорта: {article['sport']}
Ссылка: {article['url']}
{'Есть фото — макс 1000 символов!' if has_photo else 'Без фото.'}"""
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(
                    self.api_url,
                    headers={
                        "x-api-key": self.api_key,
                        "anthropic-version": "2023-06-01",
                        "content-type": "application/json",
                    },
                    json={
                        "model": "claude-sonnet-4-6",
                        "max_tokens": 600,
                        "system": SYSTEM_PROMPT,
                        "messages": [{"role": "user", "content": user_prompt}],
                    },
                )
                data = response.json()
                text = data["content"][0]["text"].strip()
                if has_photo and len(text) > MAX_CAPTION_LENGTH:
                    text = text[:MAX_CAPTION_LENGTH - 3] + "..."
                return text
        except Exception as e:
            logger.error(f"Ошибка AI: {e}")
            return self._fallback_format(article)

    def _fallback_format(self, article):
        emoji_map = {"Футбол": "⚽", "Баскетбол": "🏀", "Теннис": "🎾", "UFC/MMA": "🥊", "Общий спорт": "🏆"}
        emoji = emoji_map.get(article["sport"], "🏅")
        return (f"{emoji} <b>{article['title']}</b>\n\n"
                f"📰 {article.get('source', 'Спорт')}\n\n"
                f"🔗 <a href='{article['url']}'>Читать</a>\n\n"
                f"#спорт #новости")
