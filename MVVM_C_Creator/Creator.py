import sys
import os.path
from FileCreator import FileCreator


sceneName = input("Please enter Scene name: ")
while not len(sceneName) > 0:
	sceneName = input("Please enter Scene name: ")


projectName = input("(Optional) Please enter Project name: ")
fullUserName = input("(Optional) Please enter User name: ")
organizationName = input("(Optional) Please enter Organization Name: ")

	
documentDirectory = input("Please enter Document Directory : ")
documentDirectoryPath = os.path.dirname(os.path.realpath(documentDirectory))
isDirectory = os.path.isdir(documentDirectoryPath)

# location check
while not isDirectory:
 	documentDirectory = input("Please enter Document Directory : ")
 	documentDirectoryPath = os.path.dirname(os.path.realpath(documentDirectoryPath))
 	isDirectory = os.path.isdir(documentDirectoryPath)

# get location
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


filesFolderPath =  os.path.join(os.path.dirname(os.path.commonpath([__location__])), 'Files')

fileCreator = FileCreator(sceneName, filesFolderPath, documentDirectory, projectName, organizationName, fullUserName)
fileCreator.create()
