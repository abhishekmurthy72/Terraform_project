import requests
import os

# Fetch environment variables; do not hardcode secrets in code.
CX_REFRESH_TOKEN = os.getenv("CX_REFRESH_TOKEN", "1.AV8AY4RhO1KTpE-mfBEtooN8KT43PGlP_ONDsVbCBgsspoYAAOJfAA.BQABBAIAAAADAOz_BQD0_0V2b1N0c0FydGlmYWN0cwIAAAAAALAQM-Jr5xf5LZ0Ow7dd8PDFjoH7jUMfR6pmb6B5hIMHPRS2AmNbhhgjs1hQ_E5dOsDfuvwlAhBPMRhGdQnSS3unBWZNdfc-1U3Yt8sqe4fCAAbUMwP3dxHLUngPYaFSy59MHyYGNmVs3AR7intXVWHXQiOZJnkJy413R3V3rdL-yCuQ4ojag96Kir141Inul1w0hJR89DyD47EB4IodyXpstt6kes6idG-PhSjdlTR2gTVu6KUAYBhNib3BqN1pVnjkAnkxxFbmrb8W6OS50ItBegO6MvTYZuzVWVgQjrq6y_kXV_54wvPOksf5GSIgxGjuf6LS4BAs22b-1J3aDrA6AnGSJPlHJYTt49Sx5hrLEqToKIL-Lc3-uV6tr9vjLQsWHKIlbHuzAVvt7kbGeW2A8nhknWBT5U1VDz_3PRRML05JT0TG3eSM9vctHvb6FKqPaj7imwrQ-bLlghvjRu8Rqr-qX8yAmPhoU3L-EdobOC_pvbb4YvziTZgdkgS1AL9MNBEzdDUfMr_drvd9PNte8nFuLh3kAz-joeqVFPYe0b3Yz4i9BPiQjNSE0DfODf9it1wbx36kAGLVeSA6LPjvE2RtJeW7odu-FeVl3aEzYtcYNtUuHDpxT2fWwWL1f321A9bqTJOd0EsY5OeJPrKKP9wp1Bs_X6oFARW3wCLjMjKCM78RjJzqA2Kkz_iPN1qz88ZvJXAzXIM9e8we79wIhge3c_JLzyzEEmkh0HRVwZpmqcyS6y_C-3HBTlI_ZhOqFawx6VM1lnx8HUVtjdcDn8-IhoKuaDzf7uUAWdBtnN1SujAESMMBwX3hYz58Yrz5FJUGWaoD4Tgthm5nh9AXVklEOmwwMn5grweEVcWdmt53Wlu-ZM3oVBFVStnZhIXATq3EpOfolC_axIQXbuCqkD2_f5EWXm1logDGo0PX_pOGLgcT-58ny44vF1U8pMlbIMcyIhnxxs0wLJ6WT78mM8937UOyoQGPv7aGnIw3iFboNT9x6Te08EZu5RuE238pku1eXZscyFGJH999JRUH9wSoKQEqxdVZsIHfJde8-23k1zNGs_1dPywcLmxKqOUAVkrA_8ubq7NDXw86dX67owx_cDLLL8Kvk2Xe1EVZgxEMwjbW85m8MRf13ie2ZTUZrxQ8Qhu2_2nqgUXJ7U2sQX4EfqnSlKYQ2xsHhyIs6IQ0YfuwgboS4FF_LX30eoebiQ1Vd14VyDYG_SKZsDejSh1iH7yzJnlIqmohQ8U")  # Hardcoded refresh token
CX_TENANT = os.getenv("CX_TENANT", "maqtacxone")
AUTH_CODE = os.getenv("AUTH_CODE", "1.AV8AY4RhO1KTpE-mfBEtooN8KT43PGlP_ONDsVbCBgsspoYAAOJfAA.BQABBAIAAAADAOz_BQD0_0V2b1N0c0FydGlmYWN0cwIAAAAAALAQM-Jr5xf5LZ0Ow7dd8PDFjoH7jUMfR6pmb6B5hIMHPRS2AmNbhhgjs1hQ_E5dOsDfuvwlAhBPMRhGdQnSS3unBWZNdfc-1U3Yt8sqe4fCAAbUMwP3dxHLUngPYaFSy59MHyYGNmVs3AR7intXVWHXQiOZJnkJy413R3V3rdL-yCuQ4ojag96Kir141Inul1w0hJR89DyD47EB4IodyXpstt6kes6idG-PhSjdlTR2gTVu6KUAYBhNib3BqN1pVnjkAnkxxFbmrb8W6OS50ItBegO6MvTYZuzVWVgQjrq6y_kXV_54wvPOksf5GSIgxGjuf6LS4BAs22b-1J3aDrA6AnGSJPlHJYTt49Sx5hrLEqToKIL-Lc3-uV6tr9vjLQsWHKIlbHuzAVvt7kbGeW2A8nhknWBT5U1VDz_3PRRML05JT0TG3eSM9vctHvb6FKqPaj7imwrQ-bLlghvjRu8Rqr-qX8yAmPhoU3L-EdobOC_pvbb4YvziTZgdkgS1AL9MNBEzdDUfMr_drvd9PNte8nFuLh3kAz-joeqVFPYe0b3Yz4i9BPiQjNSE0DfODf9it1wbx36kAGLVeSA6LPjvE2RtJeW7odu-FeVl3aEzYtcYNtUuHDpxT2fWwWL1f321A9bqTJOd0EsY5OeJPrKKP9wp1Bs_X6oFARW3wCLjMjKCM78RjJzqA2Kkz_iPN1qz88ZvJXAzXIM9e8we79wIhge3c_JLzyzEEmkh0HRVwZpmqcyS6y_C-3HBTlI_ZhOqFawx6VM1lnx8HUVtjdcDn8-IhoKuaDzf7uUAWdBtnN1SujAESMMBwX3hYz58Yrz5FJUGWaoD4Tgthm5nh9AXVklEOmwwMn5grweEVcWdmt53Wlu-ZM3oVBFVStnZhIXATq3EpOfolC_axIQXbuCqkD2_f5EWXm1logDGo0PX_pOGLgcT-58ny44vF1U8pMlbIMcyIhnxxs0wLJ6WT78mM8937UOyoQGPv7aGnIw3iFboNT9x6Te08EZu5RuE238pku1eXZscyFGJH999JRUH9wSoKQEqxdVZsIHfJde8-23k1zNGs_1dPywcLmxKqOUAVkrA_8ubq7NDXw86dX67owx_cDLLL8Kvk2Xe1EVZgxEMwjbW85m8MRf13ie2ZTUZrxQ8Qhu2_2nqgUXJ7U2sQX4EfqnSlKYQ2xsHhyIs6IQ0YfuwgboS4FF_LX30eoebiQ1Vd14VyDYG_SKZsDejSh1iH7yzJnlIqmohQ8U")  # Hardcoded authCode
CHECKMARX_AUTH_URL = f"https://ind-2.iam.checkmarx.net/auth/realms/{CX_TENANT}/protocol/openid-connect/token"
CHECKMARX_API_URL = "https://ind-2.ast.checkmarx.net/api"
CODE_REPOSITORY_TYPE = "azure" #You can mention any like github/gitlab/azure/bitbucket
LOG_FILE = "refresh_log.txt"
password = "*#DSFSV KSVVDV DKSSFV"
password = "*#DSFSV KSVVDV DKSSFV"
username = "ast-app"
def get_access_token():
    """Fetch access token using refresh token."""
    data = {
        "grant_type": "refresh_token",
        "client_id": "ast-app",
        "refresh_token": CX_REFRESH_TOKEN
    }
    response = requests.post(CHECKMARX_AUTH_URL, data=data)
    if response.status_code != 200:
        print(f"❌ Failed to get access token: {response.text}")
        return None
    return response.json().get("access_token")

def get_total_projects(token):
    """Fetch total count of projects."""
    url = f"{CHECKMARX_API_URL}/projects"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Failed to fetch total project count: {response.text}")
        return 0
    
    return response.json().get("totalCount", 0)

def get_projects(token, total_count):
    """Fetch all Checkmarx projects with the correct limit."""
    url = f"{CHECKMARX_API_URL}/projects/?offset=0&limit={total_count}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Failed to fetch projects: {response.text}")
        return []
    
    return response.json().get("projects", [])

def get_scm_id(token):
    """Fetch SCM ID from Checkmarx."""
    url = f"{CHECKMARX_API_URL}/repos-manager/scms"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        for scm in response.json():
            if scm["type"].lower() == CODE_REPOSITORY_TYPE:
                return scm["id"]
    return None

def refresh_permissions(token, scm_id, project):
    """Refresh repository permissions for a given project."""
    project_id = project["id"]
    project_name = project["name"]
    repo_id = project.get("repoId") or project.get("scmRepoId")

    url = f"{CHECKMARX_API_URL}/repos-manager/scms/{scm_id}/reimport?authCode={AUTH_CODE}&projectId={project_id}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "astProjectId": project_id,
        "astProjectName": project_name,
        "repoId": repo_id,
        "scanEngines": [
            "sast", "api security", "sca"
        ],
        "importedProjectName": project_name
    }
    
    response = requests.post(url, headers=headers, json=payload)
    status_code = response.status_code
    response_json = response.json()
    
    return project_name, repo_id, status_code, response_json

def main():
    token = get_access_token()
    if not token:
        return

    total_projects = get_total_projects(token)
    if total_projects == 0:
        print("❌ No projects found.")
        return

    projects = get_projects(token, total_projects)
    scm_id = get_scm_id(token)
    if not scm_id:
        print("❌ Failed to fetch SCM ID.")
        return
    
    successful = []
    unsuccessful = []

    for project in projects:
        project_name, repo_id, status_code, response_json = refresh_permissions(token, scm_id, project)

        if status_code == 200 and "repoId" in response_json and "error" not in response_json:
            successful.append(f"✅ {project_name} (Repo ID: {repo_id}) - {status_code} - {response_json}")
        else:
            unsuccessful.append(f"❌ {project_name} (Repo ID: {repo_id}) - {status_code} - {response_json}")

    with open(LOG_FILE, "w", encoding="utf-8") as log_file:
        log_file.write("🔹 SUCCESSFUL REFRESHES 🔹\n")
        log_file.write("\n".join(successful) + "\n\n")
        log_file.write("🔻 UNSUCCESSFUL REFRESHES 🔻\n")
        log_file.write("\n".join(unsuccessful) + "\n")

    print(f"\n✅ Log file generated: {LOG_FILE}")

if __name__ == "__main__":
    main()

