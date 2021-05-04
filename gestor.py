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
	def __init__ (self, data, reg = {}):
		self.reg = reg
		self.data = data

	def download (self, path):
		for i in self.data:
			if not i in [j for j in self.reg]: self.reg [i] = {}
			for j in self.data [i]:
				if not j in [k for k in self.reg [i]]:
					mkdir (os.path.join (path, i))
					print (os.path.join (path, i, j + ".zip"))
					intermediate.download (self.data [i][j], os.path.join (path, i, j + ".zip"))
					self.reg[i][j] = True

					self.basePath, _ = os.path.split (path)
					self.extract (os.path.join (self.basePath, "installed"), i, j)

	def extract (self, path, feature, version):
		if not os.path.exists (os.path.join (path, feature, version + ".zip")):
			raise FileNotFoundError ("Packed update don't found")

		ZipFile (os.path.join (path, feature, version + ".zip")).extractall (os.path.join (path, "installed", feature, version))

	def saveReg (self):
		self.file = open (os.path.join (os.getenv ("localappdata"), "escudoweb", "data", "updaterREG.json"), "w+")
		self.file.write (json.dumps (self.reg))
		self.file.close ()