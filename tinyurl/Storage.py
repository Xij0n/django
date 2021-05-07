from collections import UserDict

class ShortUrlsStorage(UserDict):
    def __init__(self):
        super().__init__()
        self.hash_length = 2

    def to_key(self, url):
        url_hash = hash(url)
        while True:
            short_hash = url_hash % self.hash_length
            key = f'{short_hash:x}'
            saved_url = self.get(key, None)
            if saved_url is None:
                self[key] = url
                return key
            if saved_url == url:
                return key
            self.hash_length += 1



shorts = ShortUrlsStorage()