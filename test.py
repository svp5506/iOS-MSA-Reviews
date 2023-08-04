import requests
import pandas as pd

def get_reviews(page_number):
    url = f"https://itunes.apple.com/us/rss/customerreviews/page={page_number}/id=942608209/sortBy=mostRecent/json"
    response = requests.get(url)
    json_data = response.json()

    entries = json_data['feed']['entry']
    reviews = []
    for entry in entries:
        review = {
            'author_uri': entry['author']['uri']['label'],
            'author_name': entry['author']['name']['label'],
            'updated': entry['updated']['label'],
            'rating': int(entry['im:rating']['label']),
            'version': entry['im:version']['label'],
            'review_id': entry['id']['label'],
            'title': entry['title']['label'],
            'content': entry['content']['label'],
            'link': entry['link']['attributes']['href'],
        }
        reviews.append(review)

    return reviews

all_reviews = []
for page_number in range(1, 11):
    reviews = get_reviews(page_number)
    all_reviews.extend(reviews)
df = pd.DataFrame(all_reviews)
df.to_csv('reviewsRSS.csv')

