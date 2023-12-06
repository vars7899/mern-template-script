import os
import subprocess
from folderStructure import folderStructure, clientFolderStructure

def createStructure(structure, basePath = "."):
    for key, value in structure.items():
        path = os.path.join(basePath, key)
        
        if isinstance(value, dict):
            # << Create directory
            os.makedirs(path,exist_ok=True)
            createStructure(value, path)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # << Create file
            with open(path, "w") as file:
                file.write(value)
                # << Execute commands
                if key.endswith(".yarn"):
                    yarnCommand = value.strip()
                    runYarnCommand(path, yarnCommand, basePath)
    
    # << Delete yarn files
    deleteYarnFiles(basePath)

def runYarnCommand(filePath, command, basePath):
    directory = os.path.dirname(filePath)
    try:
        subprocess.run(command, cwd=os.path.join(basePath, directory), shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Yarn command in {directory}: {e}")

def deleteYarnFiles(basePath):
    for root, dirs, files in os.walk(basePath):
        for file in files:
            if file.endswith(".yarn"):
                filePath = os.path.join(root, file)
                os.remove(filePath)
                print(f"Deleted .yarn file: {filePath}")

def addClientDir(structure, basePath):
    clientPath = os.path.join(basePath + "/app/client/src")
    createStructure(structure, clientPath)


baseDirectory = os.getcwd()

createStructure(folderStructure, baseDirectory)
addClientDir(clientFolderStructure, baseDirectory)

print("""

 .----------------. .----------------. .----------------. .-----------------.
| .--------------. | .--------------. | .--------------. | .--------------. |
| | ____    ____ | | |  _________   | | |  _______     | | | ____  _____  | |
| ||_   \  /   _|| | | |_   ___  |  | | | |_   __ \    | | ||_   \|_   _| | |
| |  |   \/   |  | | |   | |_  \_|  | | |   | |__) |   | | |  |   \ | |   | |
| |  | |\  /| |  | | |   |  _|  _   | | |   |  __ /    | | |  | |\ \| |   | |
| | _| |_\/_| |_ | | |  _| |___/ |  | | |  _| |  \ \_  | | | _| |_\   |_  | |
| ||_____||_____|| | | |_________|  | | | |____| |___| | | ||_____|\____| | |
| |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' 
  
Created By Vaibhav Dhiman.
---------------------------------------------------------------------------
Do not forget to add scripts to server package.json
      """)