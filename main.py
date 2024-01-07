import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        hash_object = hashlib.md5(original_url.encode())
        short_code = hash_object.hexdigest()[:8]  # Use the first 8 characters as the short code

        self.url_mapping[short_code] = original_url
        return f"short.url/{short_code}"

    def redirect_url(self, short_code):
        original_url = self.url_mapping.get(short_code)
        if original_url:
            print(f"Redirecting to: {original_url}")
        else:
            print("Short code not found.")

def main():
    url_shortener = URLShortener()

    while True:
        print("\nOptions:")
        print("1. Shorten URL")
        print("2. Redirect URL")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            original_url = input("Enter the original URL: ")
            short_url = url_shortener.shorten_url(original_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_code = input("Enter the short code: ")
          
