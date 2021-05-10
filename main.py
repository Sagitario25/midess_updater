import intermediate
import gestor
import os
import sys
import json

def main (pasteBin = "https://pastebin.com/cYtt14fw"):
	newJson = json.loads (intermediate.getPasteBin (pasteBin))
	if os.path.exists (os.path.join (basePath, "data", "updaterREG.json")):
		regJson = json.loads (open (os.path.join (basePath, "data", "updaterREG.json"), "r").readline ())
		gest = gestor.Gestor (os.path.join (basePath), newJson, regJson)
	else:
		gest = gestor.Gestor (os.path.join (basePath), newJson)
	gest.download ()
	gest.install ()
	gest.saveReg ()
	gest.cleanDownloads ()
	gest.cleanDecompresed ()

if __name__ == "__main__":
	args = sys.argv
	if len (args) != 1:
		basePath = os.path.dirname (args [1])
	else:
		basePath = os.path.join (os.getenv ("localappdata"), "escudoweb")
		
	if not os.path.exists (os.path.join (basePath, "updates")):
		os.mkdir (os.path.join (basePath, "updates"))
	if not os.path.exists (os.path.join (basePath, "data")):
		os.mkdir (os.path.join (basePath,  "data"))
	
	main ()	