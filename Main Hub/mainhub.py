import os
import plistlib
import time

import core

#default values for mainhub class
default_values = {}
default_values['working_directory'] = os.path.dirname(os.path.realpath(__file__))
default_values['graph_directory'] = os.path.join(default_values['working_directory'], "graph.plist")
default_values['plist_error'] = "No such file or directory"
default_values['graph_content'] = {'station_1':[0,2,0,4,0], 'station_2':[0,0,2,0,0], 'station_3':[4,0,0,2,0], 'station_4':[0,4,0,0,2], 'station_5':[2,0,4,0,0]}
default_values['log_directory'] = os.path.join(default_values['working_directory'],"logs/main_hub.txt")
default_values['direction_content'] = {'station_1':{'station_2':('0x00', 20), 'station_4':('0x10', 40)}, 'station_2':{'station_3':('0x00',20)}, 'station_3':{'station_1':('0x10',40), 'station_4':('0x00',20)}, 'station_4':{'station_2':('0x10',40),'station_5':('0x00',20)}, 'station_5':{'station_1':('0x00',20), 'station_3':('0x10',40)}}
default_values['direction_directory'] = os.path.join(default_values['working_directory'], "direction.plist")

class Director(core.Core):
	def __init__(self):
		'''
		Director class communicates with GUI
		Director class takes inputs and encodes instructions to feed through wireless communication
		'''
		#class variables
		self.directions = []
		self.send_commands = []
		self.source = None
		self.destination = None
		self.number_pod = None

		#make log directory
		self.remove_directory(os.path.dirname(default_values['log_directory']))
		self.make_directory(default_values['log_directory'])

		#instantiate write
		self.f = open(default_values['log_directory'], 'w')

		#start log
		self.logger("---INITIALIZING MAINHUB DIRECTOR SYSTEM---\n")

		#import plists
		self.graph = self.import_plist(default_values['graph_directory'], default_values['graph_content'])
		self.direction = self.import_plist(default_values['direction_directory'], default_values['direction_content'])
		self.init_pods()



	def insert_station(self):
		self.logger("%s\n" % self.graph['station_1'])


	def decode_direction(self, coordinates):
		'''
		Function translate coordinates into actions
		input: 
			[station_#] to [station_#]
		returns: 
			encoded instructions
		'''
		#unpack coordinates
		source, destination = coordinates

		#return instructions
		return self.direction[source][destination]


	def get_source(self):
		'''
		Function gets source destination
		'''
		#lowercase, replace " " with "_", user input for source
		self.source = raw_input("Where would you like to start: ").replace(" ", "_").lower()

	def set_source(self, source):
		self.source = source

	def set_destination(self, destination):
		self.destination = destination


	def get_destination(self):
		'''
		function gets destination
		'''
		#lowercase, replace " " with "_", user input for destination
		self.destination = raw_input("Where would you like to go: ").replace(" ", "_").lower()


	def get_path(self):
		'''
		Function provides graphing algorithm
		'''
		#set current node to the beginning
		current_node = self.source

		#write to log
		self.logger("Start traveling from %s"  % current_node.replace("_", " "))

		#graph algorithm
		while(current_node != self.destination):
			minimum = self.graph[current_node].index(min(elem for elem in self.graph[current_node] if elem is not 0))+1
			self.directions.append((current_node, "station_%s" % minimum))
			self.logger("Moving from %s to station %s" % (current_node.replace("_"," "), minimum))
			current_node = "station_%s" % minimum
				
		#write to log
		self.logger("You have arrived at your destination.\n")


	def translate_path(self):
		'''
		Functions translates the station to station directions to motor
		'''
		#translate each instruction
		self.send_commands = []
		for elem in self.directions:
			self.send_commands.append(self.decode_direction(elem))
		#write to log
		self.logger("Path to motor function: %s\n" % self.send_commands)

		return self.send_commands
		#elem.logger("Path to motor function: %s\n" % self.send_commands)
		#self.directions = []
		#self.send_commands = []


	def close_system(self):
		'''
		Function that writes to log, to signal clean exit
		'''
		#write to log
		self.logger("---SHUTING DOWN MAINHUB DIRECTOR SYSTEM---\n")
		self.f.close()


	def init_pods(self):
		self.number_pod = input("How many pods :")
		
		while not(isinstance(self.number_pod, int)):
			self.logger("Number of pods is not valid, please input an interger")
			self.number_pod = input("How many pods :")

	def get_pod(self):
		return self.number_pod

	def get_source(self):
		return self.source