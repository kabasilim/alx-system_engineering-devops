#!/usr/bin/python3
"""This script queries the REDDIT API"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for
    a given subreddit.
    """
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus\
                5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/107.0.0.0 Mobile Safari/537.36'}

    data = requests.get("{}/r/{}/about.json"
                        .format(base_url, subreddit), headers=headers,
                        allow_redirects=False)
    if data.status_code != 200:
        return 0
    return data.json().get('data').get('subscribers')

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

