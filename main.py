import requests
from send_email import send_email
import os

topic = "tesla"

API_KEY = os.getenv("TESLA_NEWS_API_KEY")
URL = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-04&sortBy=publishedAt&" \
      "apiKey=9eb83135fd764470958dfe73d7d2ee25&language=de"

# Make request
request = requests.get(URL)

# Get a dictionary with data
content = request.json()

print(content)
# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" \
            + body + article["title"] + "\n" \
            + str(article["description"]) \
            + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)