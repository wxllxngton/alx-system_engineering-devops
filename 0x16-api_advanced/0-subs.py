#!/usr/bin/python3
"""
Script queries the Reddit API.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit.

    Parameters:
        subreddit (str): The subreddit to query.

    Returns:
        no_of_subs (int): The number of subscribers else, 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = get(url, headers=user_agent)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            all_data = response.json()
            return all_data.get("data", {}).get("subscribers", 0)
        else:
            # If the status code is not 200, return 0
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
