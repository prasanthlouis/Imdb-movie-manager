import os
import urllib
import json
import shutil
import os
import re
w=1
q=1
e=1
values=['.','[',']','(',')','m720p','480p','480','DVDSCR','BrRip','New Source','MP3','Mafiaking','1CD',
'mkv','mSD','2CD','BRRip','BRrip','720p','BluRay','YIFY','mp4','XviD','-','x264','ETRG','avi','StyLishSaLH'
,'DVD','dvd','DVDRip','RIP','rip','Rip','Back In Action']
def find(folder):
	for x in os.listdir(folder):
		#Edit to Regular Expression (Uncomment it if you want to use it.)
		'''
		if (re.search('^\s*[4-9]',x)):
			continue
		'''
		#I found this easier to implement and read though. (I removed the dirty code)
		if(x[0].isdigit() and x[0]>4):
			continue
		moviename=folder+'//'+x
		for y in range(1500,2100):
			if(str(y) in x):
				x=x.replace(str(y)," ")
		for z in values:
			if(str(z) in x):
				x=x.replace(str(z)," ")
			if("  " in x):
				x=x.replace("  "," ")
		url='http://www.omdbapi.com/?t='+str(x)
		response = urllib.urlopen(url).read()
		jsonvalues = json.loads(response)
		if jsonvalues["Response"]=="True":
			imdbrating = jsonvalues['imdbRating']
			print imdbrating+" "+x
			destinationDir = 'F:\movies\\'+ imdbrating
			if not os.path.exists(destinationDir): 
				os.makedirs(destinationDir)
			shutil.move(moviename, destinationDir)
		
		else:
			a=0
			f=1
			e=0
			g=0
			for y in range(1,5):
					x=x.replace(" ",": ",w)
					if(a==1):
						x=x.replace(":"," ",e)
					url='http://www.omdbapi.com/?t='+str(x)
					response = urllib.urlopen(url).read()
					jsonvalues = json.loads(response)
					if jsonvalues["Response"]=="True":
						imdbrating = jsonvalues['imdbRating']
						print imdbrating+" "+x
						destinationDir = 'F:\movies\\'+ imdbrating
						if not os.path.exists(destinationDir): 
							os.makedirs(destinationDir)
						shutil.move(moviename, destinationDir)
						break
					else:
						x=x.replace(": ",":",f)
						if(g>0):
							x=x.replace(" ",":",g)
						a=1
						g=g+1
						e=e+1

	
	

find('F:\movies')
