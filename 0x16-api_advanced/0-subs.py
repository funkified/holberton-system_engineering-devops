#!/usr/bin/python3
"""
Scripts that GET Reddit API
"""
import json
from requests import *


def number_of_subscribers(subreddit):
    """ GET the number of subscribers on reddit """

    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    agent = {'User-agent': 'funkified'}
    req = get(url, headers=agent)
    jreq = req.json()

    if req.status_code == 404:
        return (0)
    else:
        return (jreq['data']['subscribers'])
