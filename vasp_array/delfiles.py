#!/usr/bin/env python3
import os
from reschpc import auth
from reschpc import retrieval as ret

def readFile(filename):
    """
    Read a filename and return an array
    """
    try:
        f = open(filename,"r")
        arr  = f.readlines()
        f.close()
    except IOError:
        s = f"  Can not read {filename}"
        sys.exit(s)
    return arr

def getJobIds(arr):
    """
    Retrieve Job Ids
    """
    arrJobs=[]
    for item in arr:
        line = item.strip().split(":")
        jobid = line[5].strip()
        arrJobs.append(jobid)
    return arrJobs


if __name__ == "__main__":

    filename = "out.id.txt"
    arrLines = readFile(filename)
    arrJobIds = getJobIds(arrLines)

    TOKEN = "YOUR_TOKEN" # <---------------------
    myauth = auth.Auth(TOKEN)

    print(f"\nRESULTS::")
    for i in range(len(arrJobIds)):

        jobid = arrJobIds[i]
        print(f"Delete Job {jobid} on the Rescale Cloud Servers")
        ret.Retrieval.deleteJob(myauth, jobid)

