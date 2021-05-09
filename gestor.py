import intermediate
import os
import json
from zipfile import ZipFile
import shutil

def mkdir (newdirs):#Creation of new dirs
	absolutePath, newdirs = os.path.splitdrive (newdirs)
	for i in newdirs.split ('\\'):
		if not os.path.exists (os.path.join (absolutePath, i)):
			os.mkdir (os.path.join (absolutePath, i))

		absolutePath = os.path.join (absolutePath, i)

class Gestor:
	def __init__ (self, basePath, data, reg = {}):
		self.reg = reg
		self.data = data

		self.updatesPath = os.path.join (basePath, "updates")
		self.decompresedPath = os.path.join (basePath, "decompresed")
		self.dataPath = os.path.join (basePath, "data")
		self.installPath = os.path.join (basePath, "install")

	def download (self):
		for i in self.data:
			if not i in [j for j in self.reg]: self.reg [i] = {}
			for j in self.data [i]:
				self.needDownload = not j in [k for k in self.reg [i]]
				if not self.needDownload: self.needDownload = not self.reg [i][j]
				if self.needDownload:
					mkdir (os.path.join (self.updatesPath, i))
					intermediate.download (self.data [i][j], os.path.join (self.updatesPath, i, j + ".zip"))
					self.reg[i][j] = True

					self.extract (i, j)

	def extract (self, feature, version):
		if not os.path.exists (os.path.join (self.updatesPath, feature, version + ".zip")):
			raise FileNotFoundError ("Packed update don't found")

		ZipFile (os.path.join (self.updatesPath, feature, version + ".zip")).extractall (os.path.join (self.decompresedPath, feature, version))

	def install (self):
		for feature in os.listdir (self.decompresedPath):
			for version in os.listdir (os.path.join (self.decompresedPath, feature)):
				os.mkdir (os.path.join (self.decompresedPath, feature, version, "output"))
				if os.path.exists (os.path.join (self.decompresedPath, feature, version, "start")):
					for i in os.listdir (os.path.join (self.decompresedPath, feature, version, "start")):
						call (os.path.join (self.decompresedPath, feature, version, "start", i))
				mkdir (os.path.join (self.installPath, feature, version)) 
				copyContents (os.path.join (self.decompresedPath, feature, version, "output"), os.path.join (self.installPath, feature, version))

	def saveReg (self):
		self.file = open (os.path.join (self.dataPath, "updaterREG.json"), "w+")
		self.file.write (json.dumps (self.reg))
		self.file.close ()

	def cleanDownloads (self):
		shutil.rmtree (self.updatesPath)
		
	def cleanDecompresed (self):
		shutil.rmtree (self.decompresedPath)

def call (path, wait = True):
	if wait:
		os.system (f"start /wait {path}")
	else:
		os.startfile (path)

def copyContents (src, dest):
	for i in os.listdir (src):
		if os.path.isfile (os.path.join (src, i)):
			shutil.copyfile (os.path.join (src, i), dest)
		elif os.path.isdir (os.path.join (src, i)):
			shutil.copytree (os.path.join (src, i), dest)