#!/usr/bin/python3
"""
Script queries the Reddit API recursively,
parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""

from requests import get


def count_words(subreddit, word_list, after=None, count={}):
    """
    Recursively queries the Reddit API, parses titles of hot articles,
    and prints a sorted count of given keywords.

    Parameters:
        subreddit (str): The subreddit to query.
        word_list (list): List of keywords to count occurrences.
        after (str): Token for pagination (default is None).
        count (dict): Dictionary to store keyword counts
        (default is an empty dictionary).

    Returns:
        None: Prints keyword counts or nothing if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    word_list = [word.lower() for word in word_list]

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
                title_word_list = title.lower().split(" ")
                for word in title_word_list:
                    if word in word_list:
                        count[word] = count.get(word, 0) + 1

        if after is None:
            """Print keyword counts in descending order by count
            , then alphabetically."""
            for key in sorted(count.keys(), key=lambda k: (-count[k], k)):
                print("{}: {}".format(key, count[key]))
        else:
            return count_words(subreddit, word_list, after, count)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
