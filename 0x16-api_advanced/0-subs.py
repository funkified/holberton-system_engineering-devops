#!/bin/python3
"""
Scripts that GET Reddit API
"""
from sys import argv
import json
from requests import *


def number_of_subscribers(subreddit):
    """ GET the number of subscribers on reddit """

    url = 'https://www.reddit.com/r/' + '{}' + '/about.json'.format(subreddit)
    agent = {'User-agent': 'funkified'}
    req = get(url, headers=agent)
    jreq = req.json()

    if req.status_code == 404:
        return (0)
    else:
        return (jreq['data']['subscribers'])
