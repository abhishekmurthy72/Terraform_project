import requests
import json
import os
from datetime import datetime, timedelta, timezone

# Set up environment variables
CX_API_KEY = os.getenv('CX_API_KEY')
CX_PROJECT_ID = os.getenv('CX_PROJECT_ID')
CX_REFRESH_TOKEN = os.getenv('CX_REFRESH_TOKEN')
CX_USERNAME = os.getenv('CX_USERNAME')
CX_REPO_URL = os.getenv('CX_REPO_URL')
CX_BRANCH = os.getenv('CX_BRANCH')

# Calculate UTC epoch start and end times
utc_now = datetime.now(timezone.utc)
utc_epoch_start_time = int((utc_now + timedelta(minutes=1)).timestamp())
utc_epoch_end_time = int((utc_now + timedelta(days=1)).timestamp())

# API endpoint and headers
url = 'https://ast.checkmarx.net/api/scans'
headers = {
    'Authorization': f'Bearer {CX_REFRESH_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json; version=1.0',
    'CorrelationId': ''  # Optional: Provide a correlation ID if required
}

# Payload for the API request
payload = {
    "type": "git",
    "handler": {
        "branch": CX_BRANCH,
        "repoUrl": CX_REPO_URL,
        "credentials": {
            "username": CX_USERNAME,
            "type": "apiKey",
            "value": CX_API_KEY
        },
        "skipSubModules": False
    },
    "project": {
        "id": CX_PROJECT_ID,
        "tags": {
            "test": "",
            "priority": "high"
        }
    },
    "config": [
        {
            "type": "sast",
            "value": {
                "incremental": False,
                "presetName": "Default"
            }
        },
        {
            "type": "sca"
        },
        {
            "type": "kics"
        },
        {
            "type": "apisec"
        }
    ],
    "tags": {
        "Scheduled Scan": "",
        "priority": "high"
    },
    "cronString": "0 */3 * * * *"  # Example cron string for every 3 minutes
}

# Make the API request
try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Handle the response
    if response.status_code == 200:
        print("Scan scheduled successfully.")
    else:
        print(f"Failed to schedule scan. Status code: {response.status_code}")
        print(f"Response content: {response.content}")

except Exception as e:
    print(f"Error occurred: {e}")
