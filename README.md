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

--- 
