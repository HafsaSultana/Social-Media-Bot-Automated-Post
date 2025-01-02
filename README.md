# Social Media Auto-Posting Scheduler

This project is a Python-based script for automating the scheduling of posts to social media platforms like Facebook and LinkedIn. It reads posts from a CSV file, schedules them based on their date and time, and publishes them to the respective platforms at the specified time.

## Features
- Load configuration from a JSON file.
- Read posts, dates, and times from a CSV file.
- Schedule posts for future dates and times using the `schedule` library.
- Publish posts automatically to Facebook and LinkedIn.
- Skips posts with past timestamps.

## Prerequisites
1. Python 3.6 or later.
2. A valid Facebook Page Access Token (must have permissions to publish posts).
3. A LinkedIn Developer Account with an OAuth 2.0 Access Token.
4. Required Python libraries:
    - `facebook-sdk`
    - `schedule`
    - `requests`
    - `datetime`
    - `csv`
    - `json`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/HafsaSultana/Social-Media-Bot-Automated-Post.git
    cd social-media-auto-posting
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `config.json` file:
    ```json
    {
        "facebook_csv_path": "posts.csv",
        "facebook_page_access_token": "your_facebook_page_access_token",
        "linkedin_csv_path": "linkedin_posts.csv",
        "linkedin_access_token": "your_linkedin_access_token"
    }
    ```

4. Prepare the `posts.csv` and `linkedin_posts.csv` files:
    - Facebook posts (`posts.csv`):
      ```csv
      date,time,post_content
      2025-01-05,15:30,"Happy New Year on Facebook!"
      2025-01-06,10:00,"Check out our new Facebook features."
      ```
    - LinkedIn posts (`linkedin_posts.csv`):
      ```csv
      date,time,post_content
      2025-01-05,16:00,"Happy New Year on LinkedIn!"
      2025-01-06,11:00,"Explore our professional LinkedIn features."
      ```

## Usage

1. Run the script:
    ```bash
    python social_media_post_scheduler.py
    ```

2. The script will:
    - Load the configuration from `config.json`.
    - Read the posts from the respective CSV files.
    - Schedule and publish posts automatically to Facebook and LinkedIn.

## How It Works

1. **Loading Configurations**:
    - The script reads configurations like the CSV file paths and Access Tokens from `config.json`.

2. **Loading Posts**:
    - Reads posts from CSV files and organizes them into a list of dictionaries containing `date`, `time`, and `content`.

3. **Scheduling Posts**:
    - Posts with future dates and times are scheduled using the `schedule` library.
    - Posts with past timestamps are skipped.

4. **Publishing to Social Media**:
    - Facebook posts are published using the Facebook Graph API.
    - LinkedIn posts are published using the LinkedIn API with HTTP requests.

## Example Output
```plaintext
Scheduled Facebook post: 'Happy New Year on Facebook!' on 2025-01-05 at 15:30
Scheduled LinkedIn post: 'Happy New Year on LinkedIn!' on 2025-01-05 at 16:00
Facebook Post ID: 123456789 - Message: Happy New Year on Facebook!
LinkedIn Post ID: 987654321 - Message: Happy New Year on LinkedIn!

