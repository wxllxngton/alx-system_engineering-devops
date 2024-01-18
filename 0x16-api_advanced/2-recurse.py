#!/usr/bin/python3
"""
Script queries the Reddit API.
"""

from requests import get


def recurse(subreddit, hot_list=None, after=None):
    """
    Function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Parameters:
        subreddit (str): The subreddit to query.
        hot_list (list): List to store the titles (default is an empty list).
        after (str): Token for pagination (default is None).

    Returns:
        list or None: A list containing the titles of hot articles,
        or None if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    if hot_list is None:
        hot_list = []

    user_agent = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    params = {"show": "all", "after": after}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    try:
        response = get(url, headers=user_agent, params=params)

        if response.status_code != 200:
            return None

        all_data = response.json()
        raw_data = all_data.get("data", {}).get("children", [])
        after = all_data.get("data", {}).get("after")

        for post in raw_data:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
