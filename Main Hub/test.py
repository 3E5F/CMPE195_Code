from multiprocessing import Process, Queue
#from multiprocessing import Process
#import Queue
import time
class test(object):
	i = 1
	def __init__(self):
		self.q = Queue()

	def write_queue(self):
		while(True):
			for x in xrange(self.i):
				self.q.put("Test")
				self.i=self.i+1
			self.q.put("Boop")
			time.sleep(1)

	def check_queue(self):
		while(True):
			if self.q.empty():
				print "empty"
				time.sleep(1)
			else:
				print self.q.get()
				time.sleep(1)
				print self.q.get()
				time.sleep(1)

if __name__ == '__main__':
	t = test()
	p1 = Process(target=t.check_queue)
	p2 = Process(target=t.write_queue)
	p1.start()
	time.sleep(1)
	p2.start()