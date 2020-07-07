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

def createDir(OUTDIR,arr):

    arrDir=[]
    arrJobs=[]
    for item in arr:
        line = item.strip().split(":")
        typeid=line[1].strip()
        numnodes=line[2].strip()
        tmp=line[4].strip().split("=")
        jobid=line[5].strip()
        niter=tmp[1].strip()
        dirname = f"{OUTDIR}/{typeid}/{numnodes}/{niter}/"
        arrDir.append(dirname)
        arrJobs.append(jobid)
    return (arrJobs, arrDir)


if __name__ == "__main__":

    print(f"Retrieve files::")
    filename="out.id.txt"
    outStemDir= os.getenv("HOME") + "/Downloads/TCO/vasp/RESCALE/output/carbon-44/"
    arrLines= readFile(filename)
    (arrJobIds,arrOutputDirs)=createDir(outStemDir,arrLines)

    TOKEN = "YOUR_TOKEN"       # <------------------
    myauth = auth.Auth(TOKEN)

    print(f"\nRESULTS::")
    for i in range(len(arrJobIds)):
        print(f"  Job:'{arrJobIds[i]}' -> Output Dir.:'{arrOutputDirs[i]}'") 

        jobid=arrJobIds[i]
        # Step 1: Find ALL files linked to a JOB
        print(f"    Find ALL files linked to JOB '{jobid}'")
        (arrFileUrl, arrFileId, arrFileName,
         arrFileTypeId, arrFileIsDeleted, arrFileCheckSum) = \
            ret.Retrieval.findFilesInJob(myauth, jobid)

        # STEP 2: Download all the FILES
        outputdir=arrOutputDirs[i] 
        print(f"    Download ALL files (Tot:{len(arrFileId)}) from '{jobid}' in dir:{outputdir}\n")
        ret.Retrieval.downloadFiles(myauth, arrFileUrl, arrFileName,
                            path=outputdir, isVerbose=False)

