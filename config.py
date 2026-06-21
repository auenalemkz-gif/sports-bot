import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "15"))
MAX_CAPTION_LENGTH = 1024

RSS_FEEDS = [
    {"url": "https://rsport.ria.ru/export/rss2/archive/index.xml", "sport": "Общий спорт", "lang": "ru"},
    {"url": "https://www.sport-express.ru/export/rss/allnews.xml", "sport": "Общий спорт", "lang": "ru"},
    {"url": "https://www.championat.com/rss/index.xml", "sport": "Общий спорт", "lang": "ru"},
    {"url": "https://www.sovsport.ru/rss", "sport": "Общий спорт", "lang": "ru"},
    {"url": "https://feeds.bbci.co.uk/sport/rss.xml", "sport": "Общий спорт", "lang": "en"},
    {"url": "https://www.skysports.com/rss/12040", "sport": "Футбол", "lang": "en"},
]

SYSTEM_PROMPT = """Ты редактор спортивного Telegram-канала. Пишешь живые эмоциональные посты на русском языке. Длина 150-300 символов если есть фото, до 800 если нет. Добавляй эмодзи и 3-5 хэштегов. Формат HTML."""
