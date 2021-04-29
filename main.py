import intermediate
import os

print (intermediate.getPasteBin ("https://pastebin.com/cYtt14fw"))

if __name__ == "__main__":
	if not os.path.exists (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater")):
		os.mkdir (os.path.join (os.getenv ("localappdata"), "escudoweb", "updater"))