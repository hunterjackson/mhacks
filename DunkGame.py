import serial

ser=serial.Serial(port='COM4',timeout=3)
s = 0
while s != "\n":
	s=ser.read(1)

def Dunk_Begin():
	turn = 0
	score = 0
	pending = 0
	while turn<6: #will be while True:
		turn = turn + 1
		message=ser.read(9) #reading up to 100 bytes
		
		
		print message
		
		while message == '0,0,0,0,0': #loop that pauses the game when there is no input 
			x=0
		
		print "point\n"
		
			
		button0,button1, button2, button3, button4 = message.split(",")
		
		if button0 == "1":
			
			score = score +1
			pending = 0
		elif button1 == "1" or button2 == "1" or button3 == "1" or button4 == "1":
			if pending == 0 or pending ==1:
				pending = pending + 1 
			else:
				pending =0
				score = score + 1
		
			
	return score	

	
score = Dunk_Begin()
print "Your total score is %d" % (score)
