import os
import requests
from reschpc import auth
from reschpc import aux
from reschpc import retrieval as ret
import reschpc.manage as mg

TOKEN = "YOUR_TOKEN"      # <------

# Create Authentication Instance
myauth = auth.Auth(TOKEN)
JOBID = 'yHEBTc'          # <------

# STEP 1:List ALL Jobs:
print(f"List ALL jobs")
r=mg.Manage.listJobs(myauth)

# STEP 2: Check Job JOBID
r=mg.Manage.checkJob(myauth,JOBID)
