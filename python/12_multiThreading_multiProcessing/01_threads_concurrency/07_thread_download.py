import threading
import requests

import time

def download(url):
    print(F"Start Downloading from:{url}")
    resp= requests.get(url)
    print(F"End Downloading :{url}, size: {len(resp.content)} bytes")

urls=[
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image/webp",
]

start = time.time()

thread = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    thread.append(t)

for t in thread:
    t.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} second")
