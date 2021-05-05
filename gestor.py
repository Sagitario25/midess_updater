import intermediate
import os
import json
from zipfile import ZipFile

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

	def download (self):
		for i in self.data:
			if not i in [j for j in self.reg]: self.reg [i] = {}
			for j in self.data [i]:
				if not j in [k for k in self.reg [i]]:
					mkdir (os.path.join (self.updatesPath, i))
					intermediate.download (self.data [i][j], os.path.join (self.updatesPath, i, j + ".zip"))
					self.reg[i][j] = True

					self.extract (i, j)

	def extract (self, feature, version):
		if not os.path.exists (os.path.join (self.updatesPath, feature, version + ".zip")):
			raise FileNotFoundError ("Packed update don't found")

		print (os.path.join (self.updatesPath, feature, version + ".zip"))
		ZipFile (os.path.join (self.updatesPath, feature, version + ".zip")).extractall (os.path.join (self.decompresedPath, feature, version))

	def saveReg (self):
		self.file = open (os.path.join (self.dataPath, "updatesREG.json"), "w+")
		self.file.write (json.dumps (self.reg))
		self.file.close ()