import intermediate
import gestor
import os

import json

print (intermediate.getPasteBin ("https://pastebin.com/cYtt14fw"))

def main (pasteBin = "https://pastebin.com/cYtt14fw"):
	newJson = json.loads (intermediate.getPasteBin (pasteBin))
	if os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "data", "updaterREG.json")):
		regJson = json.loads (open (os.path.join (os.getenv ("localappdata"), "escudoweb", "data", "updaterREG.json"), "r").readline ())
		gest = gestor.Gestor (os.path.join (os.getenv ("localappdata"), "escudoweb"), newJson, regJson)
	else:
		gest = gestor.Gestor (os.path.join (os.getenv ("localappdata"), "escudoweb"), newJson)
	gest.download ()
	gest.install ()
	gest.saveReg ()
	gest.cleanDownloads ()

if __name__ == "__main__":
	if not os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "updates")):
		os.mkdir (os.path.join (os.getenv ("localappdata"), "escudoweb", "updates"))
	if not os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "data")):
		os.mkdir (os.path.join (os.getenv ("localappdata"), "escudoweb",  "data"))
	
	main ()	