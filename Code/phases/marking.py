from similarity import Similarity
from random import randint

#MAX_SIM_MARKS = 100

class Marking(Similarity):
	def __init__(self,ext, graph="PDG"):
		self.ext1 = ext
		self.ext2 = ext
		self.graph = graph
		if(ext == "mix"): #For Marking Phase check between incorr and corr
			self.ext1 = "_incorr"
			self.ext2 = "_corr"		
		self.marks = {}
		self.cluster_set_rep = []
 
	def setClusterRep(self, cluster_rep_list):
		self.cluster_set_rep = cluster_rep_list

	def grading(self, incorr_file_list, freq_nodes_list):
	
		#For each incorr file, find closest cluster using similarity value
		#The mapping obtained while calculating similarity value shows us the nodes that are found in both the cluster_rep and incorr_file   
		
		cluster_rep_incorr_mapping = []										#A list to store incorr file to cluster_rep mappings with cluster rep id
		for ind1 in xrange(len(incorr_file_list)):
			file1 = incorr_file_list[ind1]
			sim_val_list = []
			mapping_list = [] 
			for set_rep in self.cluster_set_rep:
				sim_val,mapping = self.getSimilarity(file1, set_rep)
				sim_val_list.append(sim_val)
				mapping_list.append(mapping)
				
			max_val = max(sim_val_list)									#Get maximum similarity
			argmax_id = sim_val_list.index(max_val)
			cluster_rep = self.cluster_set_rep[argmax_id]				#Find cluster rep closest to incorr_file 
			closest_mapping = dict(mapping_list[argmax_id])				#Get mapping between incorr_file and cluster_rep 
			cluster_rep_incorr_mapping.append((closest_mapping, cluster_rep)) 
			
			cluster_rep_freq_nodes = dict(freq_nodes_list[argmax_id])	#Frequency of nodes of cluster rep, higher means commonly occured node in the cluster.
			total_freq = sum(cluster_rep_freq_nodes.itervalues())
			sum_freq_incorr = 0
			for cluster_node in closest_mapping.itervalues():
				try:
					sum_freq_incorr+=cluster_rep_freq_nodes[cluster_node]	#Sometimes the node might not be in the freq dict
				except:
					continue	
				
			grade = (sum_freq_incorr/float(total_freq))
			self.marks[file1] =  grade
		return self.marks, cluster_rep_incorr_mapping
		
	def printMarks(self):
		for mark in self.marks.iteritems():
			print "Grade of %s is %f"%(mark[0].split('/')[-1], mark[1])
	
