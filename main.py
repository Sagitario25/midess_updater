import intermediate
import gestor
import os

import json

print (intermediate.getPasteBin ("https://pastebin.com/cYtt14fw"))

def main (pasteBin = "https://pastebin.com/cYtt14fw"):
	newJson = json.loads (intermediate.getPasteBin (pasteBin))
	if os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "data", "updater.json")):
		regJson = open (os.path.join (os.getenv ("localappdata"), "escudoweb", "data", "updater.json"), "r").readline ()
		gest = gestor.Gestor (newJson, regJson)
	else:
		gest = gestor.Gestor (newJson)
	gest.download (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater"))

if __name__ == "__main__":
	if not os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater")):
		os.mkdir (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater"))
	if not os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "data")):
		os.mkdir (os.path.join (os.getenv ("localappdata"), "escudoweb",  "data"))
	
	main ()	