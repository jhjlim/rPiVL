import os, time

a = 0

# hide all command line text
os.system("setterm -blank force")

# keep repeating video until a < 2
while a < 5:
	os.system("sudo omxplayer -b fish.mov")
	a = a + 1;

# after video loops unhide all cmd line text
os.system("setterm -blank poke")
