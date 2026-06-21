import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "50"))
MAX_CAPTION_LENGTH = 1024

RSS_FEEDS = [
{"url": "https://rsport.ria.ru/export/rss2/archive/index.xml", "sport": "Спорт", "lang": "ru"},
{"url": "https://www.sport-express.ru/export/rss/allnews.xml", "sport": "Футбол", "lang": "ru"},
{"url": "https://www.championat.com/rss/index.xml", "sport": "Футбол", "lang": "ru"},
{"url": "https://www.sovsport.ru/rss", "sport": "Спорт", "lang": "ru"},
{"url": "https://www.sports.ru/rss/football/", "sport": "Футбол", "lang": "ru"},
{"url": "https://www.sports.ru/rss/hockey/", "sport": "Хоккей", "lang": "ru"},
{"url": "https://www.sports.ru/rss/basketball/", "sport": "Баскетбол", "lang": "ru"},
{"url": "https://www.sports.ru/rss/mma/", "sport": "UFC/MMA", "lang": "ru"},
{"url": "https://www.sports.ru/rss/tennis/", "sport": "Теннис", "lang": "ru"},
{"url": "https://www.sports.ru/rss/formula1/", "sport": "Формула 1", "lang": "ru"},
{"url": "https://cybersport.ru/rss", "sport": "Киберспорт", "lang": "ru"},
{"url": "https://www.cybersport.com/rss", "sport": "Киберспорт", "lang": "en"},
{"url": "https://euro-football.ru/rss", "sport": "Футбол", "lang": "ru"},
{"url": "https://feeds.bbci.co.uk/sport/rss.xml", "sport": "Спорт", "lang": "en"},
{"url": "https://feeds.bbci.co.uk/sport/football/rss.xml", "sport": "Футбол", "lang": "en"},
{"url": "https://feeds.bbci.co.uk/sport/boxing/rss.xml", "sport": "Бокс", "lang": "en"},
{"url": "https://www.skysports.com/rss/12040", "sport": "Футбол", "lang": "en"},
{"url": "https://www.skysports.com/rss/12603", "sport": "UFC/MMA", "lang": "en"},
{"url": "https://www.skysports.com/rss/12008", "sport": "Теннис", "lang": "en"},
{"url": "https://www.skysports.com/rss/12010", "sport": "Формула 1", "lang": "en"},
{"url": "https://www.goal.com/feeds/en/news", "sport": "Футбол", "lang": "en"},
{"url": "https://www.espn.com/espn/rss/news", "sport": "Спорт", "lang": "en"},
{"url": "https://www.espn.com/espn/rss/soccer/news", "sport": "Футбол", "lang": "en"},
{"url": "https://www.espn.com/espn/rss/nba/news", "sport": "NBA", "lang": "en"},
{"url": "https://www.espn.com/espn/rss/nfl/news", "sport": "NFL", "lang": "en"},
{"url": "https://www.espn.com/espn/rss/tennis/news", "sport": "Теннис", "lang": "en"},
{"url": "https://www.espn.com/espn/rss/boxing/news", "sport": "Бокс", "lang": "en"},
{"url": "https://www.ufc.com/rss/news", "sport": "UFC/MMA", "lang": "en"},
{"url": "https://mmajunkie.usatoday.com/feed", "sport": "UFC/MMA", "lang": "en"},
{"url": "https://mmamania.com/rss/current", "sport": "UFC/MMA", "lang": "en"},
{"url": "https://www.nhl.com/rss/news.xml", "sport": "Хоккей", "lang": "en"},
{"url": "https://www.khl.ru/news/rss/", "sport": "Хоккей", "lang": "ru"},
{"url": "https://www.nba.com/rss/nba_rss.xml", "sport": "NBA", "lang": "en"},
{"url": "https://eurohoops.net/feed/", "sport": "Баскетбол", "lang": "en"},
{"url": "https://www.90min.com/feed", "sport": "Футбол", "lang": "en"},
{"url": "https://talksport.com/feed/", "sport": "Футбол", "lang": "en"},
{"url": "https://www.givemesport.com/feed/", "sport": "Спорт", "lang": "en"},
{"url": "https://www.fourfourtwo.com/rss", "sport": "Футбол", "lang": "en"},
{"url": "https://www.marca.com/rss/futbol.xml", "sport": "Футбол", "lang": "en"},
{"url": "https://dotesports.com/feed", "sport": "Киберспорт", "lang": "en"},
{"url": "https://www.dexerto.com/feed/", "sport": "Киберспорт", "lang": "en"},
{"url": "https://www.hltv.org/rss/news", "sport": "CS2", "lang": "en"},
{"url": "https://www.invenglobal.com/feed", "sport": "Киберспорт", "lang": "en"},
{"url": "https://afk.gg/rss", "sport": "Киберспорт", "lang": "ru"},
{"url": "https://www.formula1.com/content/fom-website/en/latest/all.html.rss.xml", "sport": "Формула 1", "lang": "en"},
{"url": "https://www.autosport.com/rss/feed/all", "sport": "Формула 1", "lang": "en"},
{"url": "https://www.boxingscene.com/boxing-rss.xml", "sport": "Бокс", "lang": "en"},
{"url": "https://fightnews.com/feed", "sport": "Бокс/MMA", "lang": "en"},
{"url": "https://www.atptour.com/en/media/rss-feed/xml-feed", "sport": "Теннис", "lang": "en"},
{"url": "https://www.wtatennis.com/feed", "sport": "Теннис", "lang": "en"},
{"url": "https://www.bleacherreport.com/articles/feed", "sport": "Спорт", "lang": "en"},
]

SYSTEM_PROMPT = """Ты редактор спортивного Telegram-канала. Пишешь живые эмоциональные посты ТОЛЬКО на русском языке. Если новость на английском — переведи и адаптируй на русский. Длина 150-300 символов если есть фото, до 800 если нет. Добавляй эмодзи и 3-5 хэштегов на русском. Формат HTML."""
