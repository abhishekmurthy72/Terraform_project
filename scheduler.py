import requests
import json
import os
from datetime import datetime, timedelta, timezone

# Set up the environment variables
CX_API_KEY = os.getenv('CX_API_KEY')
CX_PROJECT_ID = os.getenv('CX_PROJECT_ID')
CX_REFRESH_TOKEN = os.getenv('CX_REFRESH_TOKEN')
CX_USERNAME = os.getenv('CX_USERNAME')
CX_REPO_URL = os.getenv('CX_REPO_URL')
CX_BRANCH = os.getenv('CX_BRANCH')

# Calculate start time as 1 minute from now
utc_epoch_start_time = int((datetime.utcnow() + timedelta(minutes=1)).timestamp())

# Calculate end time as 24 hours from now
utc_epoch_end_time = int((datetime.utcnow() + timedelta(days=1)).timestamp())

# Headers for the request
headers = {
    'Authorization': f'Bearer {CX_REFRESH_TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json; version=1.0',
    'CorrelationId': ''  # Checkmarx may require a correlation ID
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
    "cronString": "0 */3 * * * *",  # Example cron string for every 3 minutes
    "utcEpochStartTime": utc_epoch_start_time,
    "utcEpochEndTime": utc_epoch_end_time
}

# Make the API request
try:
    response = requests.post(
        'https://ast.checkmarx.net/api/scans',
        headers=headers,
        data=json.dumps(payload)
    )

    # Handle the response
    if response.status_code == 200:
        print("Scan scheduled successfully.")
    else:
        print(f"Failed to schedule scan. Status code: {response.status_code}")
        print(f"Response content: {response.content}")

except Exception as e:
    print(f"Error occurred: {e}")
