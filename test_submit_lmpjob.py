from reschpc import auth
from reschpc import transfer as tf
from reschpc import lammps as lmp
from reschpc import manage as mg

TOKEN = "YOUR_TOKEN"          # <-----
PROJECTID = "YOUR_PROJECTID"  # <-----   

# INPUT FILES
ZIP_REPO="../data/input.zip"
LMP_INPUTFILE="in.lj.fixed"   # Contained in ZIP_REPO


# Create Authentication Instance
myauth = auth.Auth(TOKEN,PROJECTID)

# STEP 1: Upload Zip Repo
print(f"Uploading Zip Repo file to Cloud::")
ziprepo_id = tf.Transfer.upload(myauth, ZIP_REPO)
print(f"  Zip repo id:'{ziprepo_id}'")


# STEP 2: Create LAMMPS Job
print(f"Create Lammps Job::")
jobid = lmp.Lammps.create(myauth,"Testing Lammps", ziprepo_id,
                          lmpInputFile=LMP_INPUTFILE, lmpVersion="7Aug19",
                          numOfNodes=2, coresPerSlot=88 , coreType="carbon",
                          walltime=24, isVerbose=False)
print(f"  Job id:'{jobid}'")


# STEP 3: Submit Job
print(f"Submit job '{jobid}'")
mg.Manage.submit(myauth, jobid, isVerbose=False)
