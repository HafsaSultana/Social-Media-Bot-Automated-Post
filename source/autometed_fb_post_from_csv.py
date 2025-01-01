import facebook
import schedule
import json
import time
import csv
from datetime import datetime



# Load config from JSON
def load_config(config_file='config.json'):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config


# Load posts from CSV file
def load_posts(csv_file_path):
    posts = []
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            post_date = row['date']
            post_time = row['time']
            post_content = row['post_content']
            posts.append({'date': post_date, 'time': post_time, 'content': post_content})
    return posts


# Facebook post function
def post_to_facebook(message, page_access_token):
    api = facebook.GraphAPI(page_access_token)
    try:
        post = api.put_object(parent_object='me', connection_name='feed', message=message)
        print(f"Facebook Post ID: {post['id']} - Message: {message}")
    except facebook.GraphAPIError as e:
        print(f"Facebook error: {e}")
        

# Schedule posts
def schedule_facebook_posts(posts, access_token):
    for post in posts:
        post_date = post['date']
        post_time = post['time']
        message = post['content']
        post_datetime_str = f"{post_date} {post_time}"
        post_datetime = datetime.strptime(post_datetime_str, '%Y-%m-%d %H:%M')

        if post_datetime >= datetime.now():
            schedule.every().day.at(post_time).do(post_to_facebook, message=message, page_access_token=access_token).tag(post_datetime_str)
            print(f"Scheduled Facebook post: '{message}' on {post_date} at {post_time}")
        else:
            print(f"Skipped Facebook post: '{message}' scheduled for {post_date} at {post_time} (time has passed)")


# Main function
def main():
    # Load config
    config = load_config()
    
    # Load Facebook posts from CSV
    facebook_posts = load_posts(config['facebook_csv_path'])
    
    # Schedule Facebook posts
    schedule_facebook_posts(facebook_posts, config['facebook_page_access_token'])
    
    # Start the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
 