import os
import plistlib
import shutil
import time
import datetime

default_values = {}
default_values['working_directory'] = os.path.dirname(os.path.realpath(__file__))
default_values['graph_directory'] = os.path.join(default_values['working_directory'], "graph.plist")
default_values['plist_error'] = "No such file or directory"
default_values['graph_content'] = {'station_1':[0,2,0,4,0], 'station_2':[0,0,2,0,0], 'station_3':[4,0,0,2,0], 'station_4':[0,4,0,0,2], 'station_5':[2,0,4,0,0]}
default_values['log_directory'] = os.path.join(default_values['working_directory'],"logs/main_hub.txt")
default_values['direction_content'] = {'station_1':{'station_2':('0x00', 20), 'station_4':('0x10', 40)}, 'station_2':{'station_3':('0x00',20)}, 'station_3':{'station_1':('0x10',40), 'station_4':('0x00',20)}, 'station_4':{'station_2':('0x10',40),'station_5':('0x00',20)}, 'station_5':{'station_1':('0x00',20), 'station_3':('0x10',40)}}
default_values['direction_directory'] = os.path.join(default_values['working_directory'], "direction.plist")

class Core(object):
	'''
	core class that all classes should import
	'''
	def make_directory(self, directory):
		'''
		Function creates directory inside working directory
		Input: 
			folder name, created into relative directory
		'''
		self.remove_directory(directory)

		#if folder does not exist, create it
		if not(os.path.exists(os.path.dirname(directory))):
			os.makedirs(os.path.dirname(directory))

	def remove_directory(self, directory):
		'''
		'''
		if os.path.isdir(directory):
			shutil.rmtree(directory)


	def logger(self, message=''):
		'''
		Function writes messages into log files
		CAUTION: writing to file should be instantiates prior to calling this function
		Input: 
			message to be written
		'''
		#Write to log
		self.f.write("%s\t" % datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%y-%H:%M:%S'))
		self.f.write("%s\n" % message)


	def import_plist(self, plist_name, plist_content):
		'''
		Function imports plists that are needed
		Input:
			name of plist
			contents of plist
		'''
		try:
			#import
			return_info = plistlib.readPlist(os.path.join(default_values['working_directory'], plist_name))
			return return_info
		except Exception, error:
			#create plist of error matches
			if default_values['plist_error'] in error:
				self.logger("Plist does not exist, creating plist")
				plistlib.writePlist(plist_content, os.path.join(default_values['working_directory'], plist_name))
				return_info = plistlib.readPlist(os.path.join(default_values['working_directory'], plist_name))
				return return_info
			#write error if unexpected
			else:
				self.logger("ERROR IN IMPORT GRAPH: %s" % error)		