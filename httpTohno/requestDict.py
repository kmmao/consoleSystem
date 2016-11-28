#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'apple'
__mtime__ = '2016/11/19'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

class requestDict(dict):
	def __init__(self):
		pass

	def dirCreateDict(self,dirPath):
		self.__dict__={'dir':dirPath}
		return self.__dict__

	def dirDeleteDict(self,dirPath):
		self.__dict__ = {'dir': dirPath}
		return self.__dict__

	def dirRenameDict(self,parentDir,newName,oldName):
		self.__dict__ = {'parentdir': parentDir,'newname':newName,'oldname':oldName}
		return self.__dict__

	def dirScanDict(self,dirPath):
		self.__dict__ = {'dir': dirPath}
		return self.__dict__

	def fileCreateDict(self,fileEntity):
		self.__dict__ = fileEntity
		return self.__dict__

	def fileUpdateDict(self,fileEntity):
		self.__dict__ = fileEntity
		return self.__dict__

	def fileRenameDict(self,parentDir,newName,oldName):
		self.__dict__ = {'parentdir': parentDir,'newname':newName,'oldname':oldName}
		return self.__dict__

	def fileGetDict(self,filePath):
		self.__dict__ = {'file':filePath}
		return self.__dict__

	def fileGetBackupDict(self,filePath,backupfile):
		self.__dict__ = {'file':filePath,'backupfile':backupfile}
		return self.__dict__

	def fileDeleteDict(self,filePath):
		self.__dict__ = {'file':filePath}
		return self.__dict__



