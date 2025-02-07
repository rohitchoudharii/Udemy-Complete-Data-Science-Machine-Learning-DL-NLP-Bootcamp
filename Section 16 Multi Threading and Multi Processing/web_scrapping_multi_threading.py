import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://python.langchain.com/docs/versions/v0_2/overview/",
    "https://python.langchain.com/docs/versions/v0_3/",
    "https://python.langchain.com/docs/versions/v0_2/migrating_astream_events/",
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"fetched: {len(soup.text)} characters")


threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
