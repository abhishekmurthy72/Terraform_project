import os
import requests

def get_access_token(refresh_token):
    url = "https://iam.checkmarx.net/auth/realms/ps_na_miguel_gonzalez/protocol/openid-connect/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": "ast-app",
        "refresh_token": refresh_token
    }
    
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def main():
    cx_refresh_token = os.getenv('CX_REFRESH_TOKEN')
    cx_origin = os.getenv('CX_ORIGIN')
    cx_incremental_scan = os.getenv('CX_INCREMENTAL_SCAN')
    cx_project_id = os.getenv('CX_PROJECT_ID')
    cx_repo_url = os.getenv('CX_REPO_URL')
    cx_branch = os.getenv('CX_BRANCH')
    cx_commit = os.getenv('CX_COMMIT')
    cx_tag = os.getenv('CX_TAG')
    cx_credentials_username = os.getenv('CX_CREDENTIALS_USERNAME')
    cx_credentials_value = os.getenv('CX_REFRESH_TOKEN')

    # Log environment variables
    print("Environment variables:")
    print(f"CX_REFRESH_TOKEN: {cx_refresh_token}")
    print(f"CX_ORIGIN: {cx_origin}")
    print(f"CX_INCREMENTAL_SCAN: {cx_incremental_scan}")
    print(f"CX_PROJECT_ID: {cx_project_id}")
    print(f"CX_REPO_URL: {cx_repo_url}")
    print(f"CX_BRANCH: {cx_branch}")
    print(f"CX_COMMIT: {cx_commit}")
    print(f"CX_TAG: {cx_tag}")
    print(f"CX_CREDENTIALS_USERNAME: {cx_credentials_username}")
    print(f"CX_CREDENTIALS_VALUE: {cx_credentials_value}")

    try:
        # Get access token using refresh token
        access_token = get_access_token(cx_refresh_token)
        print("Access token retrieved successfully")

        # Construct the Checkmarx API request payload
        payload = {
            'type': 'gitupload',
            'handler': {
                'branch': cx_branch,
                'repoUrl': cx_repo_url,
                'credentials': {
                    'username': cx_credentials_username,
                    'type': 'apiKey',
                    'value': cx_credentials_value
                },
                'skipSubModules': True
            },
            'project': {
                'id': cx_project_id,
                'tags': {
                    'test': '',
                    'priority': 'high'
                }
            },
            'config': [
                {
                    'type': 'sast',
                    'value': {
                        'incremental': 'false',
                        'presetName': 'Default'
                    }
                }
            ],
            'tags': {
                'test': '',
                'priority': 'high'
            }
        }

        # Add commit or tag to handler if provided
        if cx_commit:
            payload['handler']['commit'] = cx_commit
        if cx_tag:
            payload['handler']['tag'] = cx_tag

        # Add incremental scan flag to config
        payload['config'][0]['value']['incremental'] = cx_incremental_scan.lower()

        # Log the payload
        print("Payload:")
        print(payload)

        # Construct headers
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json; version=1.0',
            'CorrelationId': ''
        }

        # Send the request to the Checkmarx API
        response = requests.post('https://ast.checkmarx.net/api/Scans/', headers=headers, json=payload)
        
        # Log the response status code and content
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

        response.raise_for_status()
        print("Checkmarx scan initiated successfully")
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
        print("Response content:", response.content)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
