import json
import os
from datetime import datetime, timedelta

STORAGE_FILE = "posted_urls.json"

class PostedStorage:
    def __init__(self):
        self.data = self._load()

    def _load(self):
        if os.path.exists(STORAGE_FILE):
            try:
                with open(STORAGE_FILE, "r") as f:
                    return json.load(f)
            except:
                pass
        return {}

    def _save(self):
        with open(STORAGE_FILE, "w") as f:
            json.dump(self.data, f)

    def is_posted(self, url):
        return url in self.data

    def mark_posted(self, url):
        self.data[url] = datetime.now().isoformat()
        self._save()
