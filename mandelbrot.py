import os
import numpy as np
import matplotlib.pyplot as plt

def loadSettings(filename):
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	
	settings = {}

	for line in lines[1:]:
		linesplit = line.split(";")
		if not (linesplit[0] == "" or linesplit[1] == ""):
			if not (linesplit[0] == "Niter" or linesplit[0] == "npixels"): 
				settings[linesplit[0]] = float(linesplit[1])
			else:
				settings[linesplit[0]] = int(linesplit[1])
	
	return settings

def getSettings(folder):
	filenames = os.listdir(folder)
	
	print "Choose a file:\n"
	for i in range(len(filenames)):
		print str(i + 1) + ") " + filenames[i]
	
	settingFileNumber = -1
	while settingFileNumber > len(filenames) or settingFileNumber < 0:
		settingFileNumber = int(input("File number: "))

	chosenFile = loadSettings(folder + filenames[settingFileNumber - 1])
	default = loadSettings(folder + "/defaults.csv")

	for key in chosenFile:
		default[key] = chosenFile[key]
	
	return default

def mandelBrot(x, settings):
	print "starting..."
	a = np.zeros((settings["npixels"], settings["npixels"]), dtype=complex)
	for i in range(settings["Niter"]):
		if i % 10 == 0:
			print i
		a = np.where(np.abs(a) < 1.01 * settings["Radius"], a*a + x, a)
	return a


settings = getSettings("data/")

mandelbrot = np.ones((settings["npixels"], settings["npixels"]), dtype=complex)

a = np.linspace(settings["xmin"], settings["xmax"], settings["npixels"])
b = np.linspace(settings["ymin"], settings["ymax"], settings["npixels"])

for i in range(settings["npixels"]):
	for j in range(settings["npixels"]):
		mandelbrot[i, j] = a[j] + (b[i] * 1j)
a = mandelBrot(mandelbrot, settings)
plt.imshow(np.abs(a))
plt.show()
