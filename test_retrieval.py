import os
import auth
from reschpc import retrieval as ret

TOKEN = "YOUR_TOKEN"              # <--------

# Create Authentication Instance
myauth = auth.Auth(TOKEN)
JOBID = 'uxJwQc'                  # <--------
OUTPUT_DIR = os.getenv("HOME") + "/" + "RESCALE-OUT"  # <------------

# STEP 1:Find ALL files linked to a JOB
print(f"Find ALL files linked to JOB {JOBID}")
(arrFileUrl, arrFileId, arrFileName,
 arrFileTypeId, arrFileIsDeleted, arrFileCheckSum) = \
    ret.Retrieval.findFilesInJob(myauth, JOBID)


# STEP 2: Download all the FILES
print(f"Download ALL files in dir:{OUTPUT_DIR}")
ret.Retrieval.downloadFiles(myauth, arrFileUrl, arrFileName,
                            path=OUTPUT_DIR, isVerbose=False)


# STEP 3: Delete JOBID
print(f"Delete Job {JOBID} on the Rescale Cloud Servers")
ret.Retrieval.deleteJob(myauth, JOBID)
