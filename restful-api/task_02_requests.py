#!/usr/bin/python3
"""
Module to fetch and process data from JSONPlaceholder API using requests
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints status code and titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches posts and saves selected fields (id, title, body) into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        structured_posts = []

        for post in posts:
            structured_posts.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)
