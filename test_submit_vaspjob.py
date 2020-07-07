from reschpc import auth
from reschpc import transfer as tf
from reschpc import vasp 
from reschpc import manage as mg

TOKEN = "YOUR_TOKEN"           # <----
PROJECTID = "YOUR_PROJECT_ID"  # <----

# INPUT FILES
ZIP_REPO="./data/raj.zip"


# Create Authentication Instance
myauth = auth.Auth(TOKEN,PROJECTID)

# STEP 1: Upload Zip Repo
print(f"Uploading Zip Repo file to Cloud::")
ziprepo_id = tf.Transfer.upload(myauth, ZIP_REPO)
print(f"  Zip repo id:'{ziprepo_id}'")


# STEP 2: Create LAMMPS Job
print(f"Create VASP Job::")
jobid = vasp.Vasp.create(myauth,"Testing VASP", 
                         ziprepo_id, vaspVersion='5.4.4-impi2018',
                          numOfNodes=2, coresPerSlot=240 , coreType="amberv2",
                          walltime=24, isVerbose=True)
print(f"  Job id:'{jobid}'")


# STEP 3: Submit Job
print(f"Submit job '{jobid}'")
mg.Manage.submit(myauth, jobid, isVerbose=False)
