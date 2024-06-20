#!/usr/bin/python3
"""Module for word count in all hot posts of a given Reddit subreddit"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints word count found in hot posts of a given subreddit
    Args:
        subreddit (str): The subreddit
        word_list (list): The list of words
        instances (obj): Key/value pairs of words/counts
        after (str): next page of the API results
        count (int): results matched thus far
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "webscrape:v1.0.0 (by /u/Mean-Cranberry7153)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
