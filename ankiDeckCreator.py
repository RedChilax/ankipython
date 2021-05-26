from os import listdir
from os.path import isfile , join
import shutil

#Path of IMG
path = ""

onlyfiles = [f for f in listdir(path) if isfile(join(path , f))]
print(onlyfiles)

value = 0
file = open("deck.csv" , "w")
text = ""


for element in onlyfiles :
	#Path Of Anki collection media folder
	shutil.move("img/"+element , ""+element )
	if(value % 2 == 0):
		text = "<img  src=\""+element+"\" />"
	else:

		text += ",<img  src=\""+element+"\" />"
		file.write(text+"\n")	
		print(text)
	
	
	value+=1

file.close()
	