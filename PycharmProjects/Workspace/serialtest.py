import serial
import serial.tools.list_ports
import time
import cmd


class Controller: 
	
	def __init__(self, com, speed):
		self.comport = com
		self.comspeed = speed
		
	def open(self):
		self.serial = serial.Serial(port=self.comport,baudrate=self.comspeed,timeout=5)
		
	def readline(self):
		return self.serial.readline()
		
	def write(self, str):
		self.serial.write(str)
		
	def send(self, buffer):
		send_data = ''.join(buffer)
		self.serial.write(send_data)

	def sendAndWait(self, buffer):
		self.send(buffer)
		ch = self.serial.readline()
		while ch:
			if ch.strip() == 'ok':
			   return True
			ch = self.serial.readline()
		raise Exception("Command Failed")
		
	def close(self):
		self.serial.close()
		

class Axis:

	def __init__(self, name, var, controller):
		self.name = name
		self.var = var
		self.position = 0 # in mm
		self.targetPosition = 0 # in mm`
		self.controller= controller
		self.ratio = 250 #(step / mm )
		self.headPosition = 0
		
	def setup(self):
		buffer = []
		buffer.append('%s=%d' % (self.var, self.ratio))
		self.controller.send(buffer)

	def move(self, destination):
		self.targetPosition = destination
		self.sync()

	def sync(self):
		buffer = []
		if self.position != self.targetPosition:
				if self.headPosition > 0:					
					buffer.append('G1 %s%d\n' % (self.name, self.targetPosition )) ## absolute
				else:
					buffer.append('G0 %s%d\n' % (self.name, self.targetPosition )) ## absolute
				try: 
					print buffer
					self.controller.sendAndWait(buffer)
					self.position = self.targetPosition
				except Exception,s:
					print s
					

class Console(cmd.Cmd):

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.controller = None
		self.x_axis = None
		self.y_axis = None

	def do_open(self,line):
		""" Opens a serial connection to the controller"""
		c = Controller("COM8", 115200)
		c.open()
		c.write('?')
		time.sleep(1)
		ch = c.readline()
		while ch:
			print ch 
			ch = c.readline()
		print ch
		self.controller = c
		self.x_axis = Axis('X', '$100', c)
		self.x_axis.setup()
		self.y_axis = Axis('Y', '$101', c)
		self.y_axis.setup()


	def do_moveX(self, line):
		""" Moves the X axis"""
		print line
		self.x_axis.move(int(line.strip()))
		
	def do_moveY(self, line):
		""" Moves the Y axis"""
		print line
		self.y_axis.move(int(line.strip()))
	
	 
	def do_close(self, line):
		""" Closes the serial connection """
		self.controller.close()
		self.controller = None
    
	def do_EOF(self, line):
		self.do_close()
		return True
					
					

if __name__ == '__main__':
	
	
	
	#x_axis = Axis('X','$100', c)
	#x_axis.setup()
		
	Console().cmdloop("Enter option")
		
	c.close()
