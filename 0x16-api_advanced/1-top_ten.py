#!/usr/bin/python3
"""
Scripts that GET Reddit API
"""
import json
from requests import *


def top_ten(subreddit):
    """ GET the top ten of hot post on reddit """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    agent = {'User-agent': 'funkified'}
    req = get(url, headers=agent)
    jreq = req.json()

    if req.status_code == 400:
        print(None)
    else:
        posts = jreq['data']['children']
        print(posts[i]['data']['title'] for i in range(len(posts)))
