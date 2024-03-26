#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            print("Subreddit not found.")
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)
    return 0

# Example usage:
subreddit = input("Enter subreddit name: ")
subscribers = number_of_subscribers(subreddit)
print(f"The number of subscribers in r/{subreddit} is: {subscribers}")
