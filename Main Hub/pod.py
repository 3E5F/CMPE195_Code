import core
import os
import time

default_values = {}
default_values['working_directory'] = os.path.dirname(os.path.realpath(__file__))
default_values['log_directory'] = os.path.join(default_values['working_directory'],"logs/pod_hub")

class Pod(core.Core):
	def __init__(self, pod_id):
		self.id = pod_id
		self.run = False
		self.location = "Station_1"
		self.speed = 0
		self.proximity = 0

		#test
		self.counter = 5

		#instantiate write
		self.f = open("%s%s.txt" % (default_values['log_directory'], pod_id), 'wb')

		#start log
		self.logger("---INITIALIZING POD SYSTEM---\n")


	def get_id(self):
		return self.id

	def set_id(self, pod_id=0):
		self.id = pod_id

	def get_run(self):
		return self.run

	def set_run(self, flag=False):
		self.run = flag

	def get_location(self):
		return self.location

	def set_location(self, region=None):
		self.location = region

	def get_speed(self):
		return self.speed

	def set_speed(self, speed):
		self.speed = speed

	def get_proximity(self):
		return self.proximity

	def set_proximity(self, proximity):
		self.proximity = proximity

	def close_system(self):
		'''
		Function that writes to log, to signal clean exit
		'''
		#write to log
		self.logger("---SHUTING DOWN POD SYSTEM---\n")
		self.f.close()

	def report(self):
		self.logger("id: %s" % self.get_id())
		self.logger("run: %s" % self.get_run())
		self.logger("loc: %s" % self.get_location())
		self.logger("spd: %s" % self.get_speed())
		self.logger("prx: %s\n" % self.get_proximity())
		time.sleep(1)

	def set(self, pod_id=None, pod_run=None, pod_location=None, pod_speed=None, pod_proximity=None):
		if pod_id != None:
			self.set_id(pod_id)
		if pod_run != None:
			self.set_run(pod_run)
		if pod_location != None:
			self.set_location(pod_location)
		if pod_speed != None:
			self.set_speed(pod_speed)
		if pod_proximity != None:
			self.set_proximity(pod_proximity)

	def finish_run(self):
		self.set_run(False)
		self.set_location()