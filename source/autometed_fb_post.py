from datetime import datetime
import facebook
import time

# Use your valid Page Access Token here (make sure it has the required permissions)
page_access_token = 'YOUR_PAGE_ACCESS_TOKEN'

# Initialize the Graph API with the page access token
api = facebook.GraphAPI(page_access_token)

# Define your scheduled time in 'YYYY-MM-DD HH:MM:SS' format
scheduled_time = '2024-10-9 19:00:00'  # Example time: October 9, 2024, 7:00 PM

# Convert the scheduled time to a UNIX timestamp (required by the API for scheduling)
scheduled_timestamp = int(time.mktime(datetime.strptime(scheduled_time, '%Y-%m-%d %H:%M:%S').timetuple()))

# Post a message to the page's feed (schedule the post)
post = api.put_object(
    parent_object='me',                  # Post to the page
    connection_name='feed',              # The connection (feed)
    message="Automated final post via Python!",  # The post message
    scheduled_publish_time=scheduled_timestamp,  # Schedule for a future time
    published=False                      # Set to False to schedule, not publish immediately
)

# Print the ID of the scheduled post
print("Scheduled Post ID:", post['id'])
