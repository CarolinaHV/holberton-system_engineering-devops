#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    ''' Finds the number of subscribers in a subreddit '''

    header = {'User-Agent':  'Chrome/91.0.4472.77 Safari/537.36'}
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=header)

    if response.status_code == 404:
        return 0
    subscribers = response.json().get('data').get('subscribers')
    return subscribers
