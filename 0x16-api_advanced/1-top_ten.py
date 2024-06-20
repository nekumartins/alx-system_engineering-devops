#!/usr/bin/python3
"""Module to print hot posts on a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "webscrape:v1.0.0 (by /u/Mean-Cranberry7153)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
