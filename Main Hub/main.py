from PySide import QtCore, QtGui
import sys
import os
import temp
from multiprocessing import Process, Queue
import datetime
import time

import mainhub
import pod

default_values = {}

started = False

#testing
count = 0
test_file = None

class Main(object):
	def __init__(self):
		self.ex = None
		self.app = None
		self.queue = Queue()
		self.p1 = None
		self.p2 = None
		self.set = False
		self.pod_list = []
		self.director = None


	def gui_start(self):
		self.app = QtGui.QApplication(sys.argv)
		self.ex = temp.GUI()
		self.ex.confirm_signal.connect(self.push_queue)
		self.ex.close_signal.connect(self.close_system)
		self.ex.setWindowTitle("Spartan Superway Ticket System")  
		self.ex.setWindowFlags(self.ex.windowFlags() | QtCore.Qt.CustomizeWindowHint) 
		self.ex.setWindowFlags(self.ex.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
		self.ex.setWindowFlags(self.ex.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
		self.ex.show()
		sys.exit(self.app.exec_())


	def push_queue(self):
		self.queue.put((self.ex.source, self.ex.destination))
		print("%s\tCoordinates Pushed" % datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%y-%H:%M:%S'))
		#print "Coordinates Pushed"


	def close_system(self):
		self.queue.put(("system_close", None))
		self.ex.close_system()
		self.app.quit()

	def shutdown(self):
		self.director.close_system()
		for elem in self.pod_list:
			elem.close_system()	
		exit()


	def main_hub(self):
		self.director = mainhub.Director(4)

		for elem in range(self.director.get_pod()):
			self.pod_list.append(pod.Pod(elem))

		while(True):
			if self.queue.empty():
				print("%s\tCurrent State: REPORT" % datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%y-%H:%M:%S'))
				for elem in self.pod_list:
					elem.report()
			else:

				current = self.queue.get()
				if "system_close" in current:
					print("%s\tCurrent State: SHUTDOWN" % datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%y-%H:%M:%S'))
					self.shutdown()
				elif not(None in current):
					print("%s\tCurrent State: DIRECTOR" % datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%y-%H:%M:%S'))
					(source, destination) = current
					#print("%s-%s" % (source, destination))
					print("%s\t%s-%s" % (datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%y-%H:%M:%S'), source, destination))
					self.director.set_source(source)
					self.director.set_destination(destination)
					self.director.get_path()
					for elem in self.pod_list:
						if elem.get_run() == False:
							directions = self.director.translate_path()
							elem.set_run(True)
							elem.logger(directions)
							break

			#TEST
			for elem in self.pod_list:
				if elem.get_run() == True and elem.counter > 0:
					elem.counter -= 1
				elif elem.counter == 0:
					elem.set(pod_location=destination)
					elem.finish_run()

	def test(self):
		self.p1 = Process(target=self.main_hub)
		self.p2 = Process(target=self.gui_start)
		self.p1.start()
		time.sleep(3)
		self.p2.start()


if __name__ == '__main__':
	maintest = Main()
	maintest.test()