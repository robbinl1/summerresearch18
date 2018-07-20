'''
Lauren Robbins
pythonserver.py
This program loads a keras model, recieves an image, runs a prediction on that image,
then moves the item to another folder.
'''
#Import(ant) statements
from __future__ import print_function
import keras
from keras.models import Sequential, load_model
import keras.preprocessing.image as img
import socket
import shutil

#Open socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 6457))
s.listen(5)
destfolder = "predict/dummyclass"

#Load model
mymodel = load_model("facultycnnmodel.h5")
print("Model Loaded")

#recieve and predict
while True:
	c, addr = s. accept()
	print("Connected")
	field="newendoffieldstring".encode('utf-8')
	eof = "newendoffilestring"
	eof = eof.encode('utf-8')
	file = c.recv(1024)
	found = file.find(eof)
	while found == -1:
		file = file + c.recv(1024)
		found = file.find(eof)
	fieldindex = file.find(field)
	filename= file[:fieldindex]
	dst = destfolder+filename
	file = file[fieldindex+len(field):-(len(eof))]
	newfile = open(dst, "wb")
	newfile.write(file)
	newfile.close()
	c.close()
	predict_datagen = img.ImageDataGenerator(rescale=1./255)
	test_generator = predict_datagen.flow_from_directory(
		"predict", target_size=(640, 480), batch_size=1)
	shutil.move("predict/dummyclass"+filename, "finished/"+filename)
	myarray=mymodel.predict_generator(test_generator, verbose=1)
	print(myarray)

s.close()
