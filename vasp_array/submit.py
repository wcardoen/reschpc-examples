import os
from datetime import datetime
from reschpc import auth
from reschpc import transfer as tf
from reschpc import manage as mg
from reschpc import vasp

TOKEN = "YOUR_TOKEN"           # <-----
PROJECTID = "YOUR PROJECT_ID"  # <----

INPUT_DIR= os.getenv("HOME") + "/Downloads/TCO/vasp/RESCALE/input/"
MAX_ITER=6

# INPUT Files + their corresponding ids
arr_ziprepo=[ INPUT_DIR + "medium.zip"]
arr_ziprepo_id=[]
arr_ziplabel=['medium']

# List of CLUSTER SIZE
arr_clustersize=[2,4,6,8,10,12,14,16,18,20]


# Create Authentication Instance
myauth = auth.Auth(TOKEN,PROJECTID) 


print(f"START: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# Step 1: Upload Zip Repos
print(f"Uploading Zip Repo files to Cloud::")
for item in arr_ziprepo:
    ziprepo_id = tf.Transfer.upload(myauth, item)
    print(f"  Zip file:{item} -> repo id:'{ziprepo_id}'")
    arr_ziprepo_id.append(ziprepo_id)


# Step 2: Create jobs + submit them
print(f"\nCreate & submit VASP Jobs::")
for i, ziprepo_id in enumerate(arr_ziprepo_id):
    for numnodes in arr_clustersize:
        numcores = 44 * numnodes

        for niter in range(1,MAX_ITER+1):
            jobname="VASP:" + arr_ziplabel[i] + ":" + \
                              str(numnodes) + ":" + str(numcores) + ":" \
                              "iter=" + str(niter)   

            # Create a Job
            jobid = vasp.Vasp.create(myauth, jobname,
                                     ziprepo_id, vaspVersion='5.4.4-impi2018',
                                     numOfNodes=numnodes, coresPerSlot=numcores , coreType="carbon",
                                     walltime=2, isVerbose=False)
            print(f"{jobname}:{jobid}") 

            # Submit the corresponding job
            mg.Manage.submit(myauth, jobid, isVerbose=False)

print(f"END: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

