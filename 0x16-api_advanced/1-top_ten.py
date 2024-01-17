#!/usr/bin/python3
"""
Script queries the Reddit API.
"""

from requests import get


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Parameters:
        subreddit (str): The subreddit to query.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    params = {"limit": 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    try:
        response = get(url, headers=user_agent, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            all_data = response.json()
            posts = all_data.get("data", {}).get("children", [])

            for post in posts:
                # Check if the "title" key exists before accessing it
                title = post.get("data", {}).get(
                    "title", "Title not available"
                )
                print(title)

        else:
            # If the status code is not 200, print "None"
            print("None")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("None")
