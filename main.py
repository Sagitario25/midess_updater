import intermediate
import gestor
import os

import json

print (intermediate.getPasteBin ("https://pastebin.com/cYtt14fw"))

def main (pasteBin = "https://pastebin.com/cYtt14fw"):
	newJson = json.loads (intermediate.getPasteBin (pasteBin))
	if os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "data", "updaterREG.json")):
		regJson = json.loads (open (os.path.join (os.getenv ("localappdata"), "escudoweb", "data", "updaterREG.json"), "r").readline ())
		gest = gestor.Gestor (newJson, regJson)
	else:
		gest = gestor.Gestor (newJson)
	gest.download (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater"))


	gest.saveReg ()

if __name__ == "__main__":
	if not os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater")):
		os.mkdir (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater"))
	if not os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "data")):
		os.mkdir (os.path.join (os.getenv ("localappdata"), "escudoweb",  "data"))
	
	main ()	