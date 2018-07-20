from picamera import PiCamera
from time import sleep
import socket
def take(filename):
	camera = PiCamera()
	camera.start_preview()
	sleep(2)
	camera.resolution="640x480"
	camera.capture("static/"+filename)
	print("captured")
	camera.stop_preview()
	camera.close()
	return

def send(filename):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ip = "hephaestus.wlaruba4.denison.edu" #insert ip
	#ip= "140.141.207.224"
	s.connect((ip, 6457))
	field="newendoffieldstring".encode('utf-8')
	eof="newendoffilestring"
	eof = eof.encode('utf-8')
	openfile = open("static/"+filename, "rb")
	file = openfile.read()
	file = filename.encode('utf-8') + field + file + eof
	s.send(file)
	s.close()
