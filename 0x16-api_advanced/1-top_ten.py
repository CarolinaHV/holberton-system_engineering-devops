#!/usr/bin/python3
"""
Finds and prints the titles of the first 10 host posts

"""
import requests


def top_ten(subreddit):
    header = {'User-Agent':  'Chrome/66.0.3359.139 Mobile Safari/537.36'}
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=header, params={'limit': 10},
                            allow_redirects=False)

    if response.status_code == 404:
        print(None)
    else:
        response = response.json()
        lists = [h for j, h in response.items() if j == 'data']
        lists = lists[0].get('children')
        for l in lists:
            print(l.get('data').get('title'))
