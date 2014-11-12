import time
import mainhub
import pod
from PySide import QtCore, QtGui
import sys
import os
import temp
import Queue

default_values = {}
default_values['stop_system'] = "stop_system"
default_values['insert_station'] = "insert_station"

pod_list=[]
queue = Queue.Queue()

#testing
count = 0

def derp():
	print 'Hi'
	mySource = ex.source
	myDestination = ex.destination
	print "Main Source - " + mySource
	print "Main Destination - " + mySource

#app = QtGui.QApplication(sys.argv)
#ex = temp.MainWindow()
#ex.pushed.connect(derp)
#ex.setWindowTitle("Spartan Superway Ticket System")
#ex.show()
#sys.exit(app.exec_())




if __name__ == "__main__":
	try:
		director = mainhub.Director()
		#gui = temp.MainWindow()
		#gui.main()
		#temp.main()
		

		#while queue.empty():
		for elem in range(director.get_pod()):
			pod_list.append(pod.Pod(elem))

		while(True):
			if queue.empty():
				for elem in pod_list:
					elem.report()
			elif not(queue.empty()):
				(source, destination) = queue.get()
				director.set_source(source)
				director.set_destination(destination)
				if director.get_source() == default_values['stop_system']:
					director.close_system()
					for elem in pod_list:
						elem.close_system()
					exit()
				else:
					director.get_path()
					for elem in pod_list:
						if elem.get_run() == False:
							directions = director.translate_path()
							elem.set_run(True)
							elem.logger(directions)
							break
			#test
			count = count + 1
			if count == 3:
				queue.put(("station_1", "station_5"))
			elif count == 5:
				queue.put(("station_5", "station_1"))
			elif count == 7:
				queue.put(("stop_system", None))

	except Exception, error:
		director.logger("ERROR IN SYSTEM: %s" % error)