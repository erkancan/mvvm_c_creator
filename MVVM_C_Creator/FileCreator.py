import sys
import re
import os.path
from shutil import copyfile
from time import gmtime, strftime

class FileCreator(object):

	FILENAME = '___FILENAME___'
	PROJECTNAME = '___PROJECTNAME___'
	FULLUSERNAME = '___FULLUSERNAME___'
	DATE = '___DATE___'
	YEAR = '___YEAR___'
	ORGANIZATIONNAME = '___ORGANIZATIONNAME___'
	VARIABLE_sceneName = '___VARIABLE_sceneName___'

	"""docstring for CoordinatorCreator"""
	def __init__(self, sceneName, sourcePath, directionPath,
		projectName, organizationName, fullUsername):
		super(FileCreator, self).__init__()
		self.sceneName = sceneName
		self.sourcePath = sourcePath
		self.directionPath = directionPath
		self.projectName = projectName
		self.organizationName = organizationName
		self.fullUsername = fullUsername
	
	@property
	def filesPaths(self):
		return ['{}'.format(os.path.join(self.sourcePath, '___FILEBASENAME___Coordinator.swift')),
		'{}'.format(os.path.join(self.sourcePath, '___FILEBASENAME___View.swift')),
		'{}'.format(os.path.join(self.sourcePath, '___FILEBASENAME___ViewController.swift')),
		'{}'.format(os.path.join(self.sourcePath, '___FILEBASENAME___ViewModel.swift'))]

	@property
	def directionPaths(self):
		return ['{}'.format(os.path.join(self.directionPath, '{}Coordinator.swift'.format(self.sceneName))),
		'{}'.format(os.path.join(self.directionPath, '{}View.swift'.format(self.sceneName))),
		'{}'.format(os.path.join(self.directionPath, '{}ViewController.swift'.format(self.sceneName))),
		'{}'.format(os.path.join(self.directionPath, '{}ViewModel.swift'.format(self.sceneName)))]

	@property
	def fileNames(self):
		return ['{}Coordinator.swift'.format(self.sceneName),
		'{}View.swift'.format(self.sceneName),
		'{}ViewController.swift'.format(self.sceneName),
		'{}ViewModel.swift'.format(self.sceneName)]

	def create(self):
		count = 0
		for path in self.directionPaths:
			directionFile = open(path, "w")
			sourceFile = open(self.filesPaths[count], "r")
			lines =  sourceFile.readlines()
			
			for line in lines:
				line = line.replace(self.FILENAME, self.fileNames[count])
				line = line.replace(self.PROJECTNAME, self.projectName)
				line = line.replace(self.FULLUSERNAME, self.fullUsername)
				line = line.replace(self.DATE, strftime("%Y-%m-%d", gmtime()))
				line = line.replace(self.YEAR, strftime("%Y", gmtime()))
				line = line.replace(self.ORGANIZATIONNAME, self.organizationName)
				line = line.replace(self.VARIABLE_sceneName, self.sceneName)
				directionFile.write(line)
		
			count += 1
			directionFile.close()
			sourceFile.close()
			

			



		
