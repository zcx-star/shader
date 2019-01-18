import os

shaderPath = r"D:\Roboto\Data\Source\Shaders\World" 
versionFile = r"D:\star\shader\static\shader\python\headVersions.txt"

def getFileNames(path):
    fileNames = []
    for i,j,k in os.walk(path):
        for kk in k:
            if kk.endswith("dbx"):
                fileNames.append(kk[:-4])
    return fileNames

def getFilePaths(path):
    filePaths = []
    for i,j,k in os.walk(path):
        for kk in k:
            if kk.endswith("dbx"):
                filePaths.append(os.path.join(i,kk))
    return filePaths 

def getHeadVersion(path):
    filePaths = getFilePaths(path) 
    headVersions = []
    for f in filePaths:
        cmd = "p4 filelog "+ f +"#have,#head"
        result = os.popen(cmd).readlines()
        if len(result)>0:            
            headVersions.append(result[1].split(' ')[1][1:])
        else:
            headVersions.append("10000")
        result = []
    return headVersions

def writeToTxt(nameList,versionList):
    f = open(versionFile, 'w')
    for i in range(len(nameList)):
        f.write( nameList[i] + '_' + versionList[i] + '\n')
    f.close()

shaderNames = getFileNames(shaderPath)
headVersions = getHeadVersion(shaderPath)
writeToTxt(shaderNames,headVersions)