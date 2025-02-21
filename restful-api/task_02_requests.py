#!/usr/bin/python3
"""
This script fetches the list of posts from https://jsonplaceholder.typicode.com/posts
and prints their titles.
It also saves the list of posts to a CSV file named "posts.csv"."""
import requests
import csv

def fetch_and_print_posts():
    """
    Fetches the list of posts from https://jsonplaceholder.typicode.com/posts and
    prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Extract relevant data
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        
        # Write to CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
        
        print("Posts saved to posts.csv")
    else:
        print("Failed to fetch posts.")

# Run functions
fetch_and_print_posts()
fetch_and_save_posts()


