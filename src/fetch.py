import requests

def fetch():
    return requests.get("https://example.com").status_code

if __name__ == "__main__":
    print(fetch())
