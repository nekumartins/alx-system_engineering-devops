#!/usr/bin/python3
"""Module to Query subscribers on a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "webscrape:v1.0.0 (by /u/Mean-Cranberry7153)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
