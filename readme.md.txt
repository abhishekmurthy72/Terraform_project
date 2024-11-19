<b>GITHUB ACTIONS SECHEDULER FOR CHECKMARX REPO SCANS</b>

Description: This projects help you in setting up the github action for scheduling the checkmarx scanner.

Steps to setup: 
1) Copy the scheduler.py file in the root directory of your repo.
2) Copy the cx-scheduler workflow file in the .github/workflows/ directory.
3) You need to set the cron timing as per your requirement minimum 1hour/1 day/Weekend/Or a day as tested in the cxone-scheduler.yml file under schedule.
4) You require to declare the below environment variables and the secrets in your git settings >> security >> Secrets & variables >> Actions.
          env:
            ${{ secrets.CX_API_KEY }}
            ${{ secrets.CX_PROJECT_ID }}
            ${{vars.GIT_PORJECT_NAME}}
            ${{ vars.GIT_REPO_URL }}
            ${{vars.GIT_DEFAULT_BRANCH}}
            ${{ vars.GIT_USEREMAIL }}
            ${{ secrets.GIT_API_KEY_TOKEN }}
5) The scheduler.py uses the python inbuilt requests library to request respone from the API URL for triggering a scan "https://ast.checkmarx.net/api/scans". 
6) You can view the scheduler in the actions page. >> https://github.com/<username>/<reponame>/actions/workflows/cxone-scheduler.yml
7) You can view the latests scan in the checkmarx UI of that specific project.