import os
import requests

def main():
    cx_api_key = os.getenv('CX_API_KEY')
    cx_origin = os.getenv('CX_ORIGIN')
    cx_incremental_scan = os.getenv('CX_INCREMENTAL_SCAN')
    cx_project_name = os.getenv('CX_PROJECT_NAME')
    cx_repo_url = os.getenv('CX_REPO_URL')
    cx_branch = os.getenv('CX_BRANCH')

    # Log environment variables
    print("Environment variables:")
    print(f"CX_API_KEY: {cx_api_key}")
    print(f"CX_ORIGIN: {cx_origin}")
    print(f"CX_INCREMENTAL_SCAN: {cx_incremental_scan}")
    print(f"CX_PROJECT_NAME: {cx_project_name}")
    print(f"CX_REPO_URL: {cx_repo_url}")
    print(f"CX_BRANCH: {cx_branch}")

    # Construct the Checkmarx API request
    headers = {
        'Authorization': f'Bearer {cx_api_key}',
        'Content-Type': 'application/json',
        'Accept': 'application/json; version=1.0',
        'CorrelationId': ''
    }

    payload = {
        'origin': cx_origin,
        'incrementalScan': cx_incremental_scan,
        'projectName': cx_project_name,
        'repoURL': cx_repo_url,
        'branch': cx_branch
    }

    # Log the headers and payload
    print("Headers:")
    print(headers)
    print("Payload:")
    print(payload)

    # Send the request to the Checkmarx API
    response = requests.post('https://ast.checkmarx.net/api/scans', headers=headers, json=payload)
    
    # Log the response status code and content
    print("Response status code:", response.status_code)
    print("Response content:", response.text)

    try:
        response.raise_for_status()
        print("Checkmarx scan initiated successfully")
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError: {e}")
        print("Response content:", response.content)

if __name__ == "__main__":
    main()
