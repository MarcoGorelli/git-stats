import requests
import os

data = requests.get('https://api.github.com/search/issues?q=is:pr+repo:pandas-dev/pandas+author:marcogorelli+is:merged').json()

print(f"Merged PRs: {data['total_count']}")

url = 'https://api.github.com/graphql'
query = (
"""
{
  user(login: "marcogorelli") {
    contributionsCollection {
      pullRequestReviewContributionsByRepository {
        contributions {
          totalCount
        }
        repository {
          name
        }
      }
    }
  }
}
"""
)
json = { 'query' : query}
api_token = os.environ['GITSTATS_TOKEN']
headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=json, headers=headers)

json_data = r.json()['data']['user']['contributionsCollection']['pullRequestReviewContributionsByRepository']

reviews = [i['contributions']['totalCount'] for i in json_data if i['repository']['name'] == 'pandas'][0]

print(f'Number of reviews: {reviews}')