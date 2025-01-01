from datetime import datetime
import requests
import json



# Replace these with your LinkedIn API credentials
access_token = 'YOUR_ACCESS_TOKEN'
linkedin_api_url = 'https://api.linkedin.com/v2/ugcPosts'

# Define the headers including your access token for authorization
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'X-Restli-Protocol-Version': '2.0.0',
}

# Define your post content
post_message = "Automated LinkedIn post via Python!"

# Define your API request body
post_data = {
    "author": "urn:li:person:YOUR_PERSON_URN",  # Your LinkedIn Person URN
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": post_message,
            },
            "shareMediaCategory": "NONE",
        },
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC",
    },
}

# Send the POST request to the LinkedIn API
response = requests.post(linkedin_api_url, headers=headers, data=json.dumps(post_data))

# Check for successful response and print the result
if response.status_code == 201:
    print("Post successfully created:", response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
