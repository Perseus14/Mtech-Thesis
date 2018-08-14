import community
import networkx as nx
from itertools import combinations
from collections import defaultdict
import numpy as np
from sklearn.cluster import SpectralClustering
from sklearn import metrics

class Cluster:
	def __init__(self):
		self.cluster_set = []
	
	def getThreshold(self, similarity_measure_list):
		total_sum = 0
		for ele in similarity_measure_list:
			total_sum+=ele[2]
		return (total_sum)/float(len(similarity_measure_list))

	def louvianClustering(self, similarity_measure_list):
		edge_list = []
		node_list = []
		thresh = 0#self.getThreshold(similarity_measure_list)
		for element in similarity_measure_list:
			f1,f2,val = element
			if(float(val)>thresh):
				edge_list.append((f1,f2,float(val)))
			node_list.append(f1)
			node_list.append(f2)
		node_list = list(set(node_list))
		G = nx.Graph()
		G.add_nodes_from(node_list)
		G.add_weighted_edges_from(edge_list)

		partition= community.best_partition(G)
		dendo = community.generate_dendrogram(G,None,'weight',1.,False)
		testing= community.partition_at_level(dendo, len(dendo) - 1)
		res = community.modularity(partition,G,'weight');

		list1 = [partition]
		cluster_set = set(val for dic in list1 for val in dic.values())
		cluster_set_elements = []
		for cluster_id in cluster_set:
			temp_elements = []
			for node,cluster in partition.iteritems():
				if(cluster==cluster_id):
					temp_elements.append(node)
			cluster_set_elements.append(temp_elements)
		self.cluster_set = cluster_set_elements		
		return cluster_set_elements
		
	def ipca(self, similarity_measure_list):
		T_IN = 0.5
		data = defaultdict(set) # node id => neighboring node ids
		global_edges, degrees = defaultdict(dict), defaultdict(float)
		for line in similarity_measure_list:
			a,b,w = line
			w = float(w)
			data[a].add(b)
			data[b].add(a)
			global_edges[a][b], global_edges[b][a] = w, w
			degrees[a] += w
			degrees[b] += w
		weights = defaultdict(int)
		for a,b in combinations(data, 2):
			if b not in data[a]: continue	
			shared = len(data[a] & data[b])
			weights[a] += shared
			weights[b] += shared

		unvisited = set(data)
		num_clusters = 0

		# DIFFERENT: weighted degrees
		seed_nodes = sorted(data,key=lambda k: (weights[k],degrees[k]),reverse=True)
		cluster_set = []
		for seed in seed_nodes: # get highest weight/degree node
			if seed not in unvisited: continue

			cluster = set((seed,))

			while True:
				# DIFFERENT: rank neighbors by the sum of global edge weights
				# between the node and cluster nodes
				frontier = sorted((sum(global_edges[p][c] for c in data[p] & cluster),p)
					for p in set.union(*((data[n] - cluster) for n in cluster)))

				# do this until IN_vK < T_IN, SP <= 2 is met, or no frontier nodes left
				found = False
				while frontier and not found:
					m_vk,p = frontier.pop()
					if m_vk < T_IN * len(cluster): break
					c_2neighbors = data[p] & cluster
					c_2neighbors.update(*(data[c] & cluster for c in c_2neighbors))
					if cluster == c_2neighbors:
					 	found = True
					 	break

				if not found: break
				
				cluster.add(p) # otherwise, add the node to the cluster

			unvisited -= cluster
			if len(cluster) > 1:
				print ' '.join(cluster)

				num_clusters += 1
				print num_clusters, len(cluster), len(unvisited)
				cluster_set.append(list(cluster))

			if not unvisited: break	
		#self.cluster_set = cluster_set	
		return cluster_set
	
	def spectralClustering(self, similarity_measure_list, n_clusters=2):
		sim_dict = {}
		edge_set = set()
		for (file1, file2, val) in similarity_measure_list:
			sim_dict[(file1,file2)] = val
			sim_dict[(file2,file1)] = val
			edge_set.add(file1)
			edge_set.add(file2)
			
		edge_list = list(edge_set)
		affinity_matrix = []
		for edge_id_x in xrange(len(edge_list)):
			temp = []
			for edge_id_y in xrange(len(edge_list)):
				try:
					temp.append(sim_dict[(edge_list[edge_id_x], edge_list[edge_id_y])])
				except:
					temp.append(0)	
			affinity_matrix.append(temp)
		affinity_matrix = np.array(affinity_matrix)
		
		sc = SpectralClustering(n_clusters, affinity='precomputed', n_init=100)
		sc.fit(affinity_matrix)
		labels = sc.labels_
		n_cluster = len(set(labels))
		cluster_set = []
		for x in xrange(n_cluster):
			cluster_set.append([])
		
		for x in xrange(len(labels)):
			cluster_set[labels[x]].append(edge_list[x])
		
		#self.cluster_set = cluster_set			 
		return cluster_set
			
	def printCluster(self):
		for cluster_id in xrange(len(self.cluster_set)):
			print "Cluster:",cluster_id,"\n", self.cluster_set[cluster_id], "\n"
	
	def cluster_louvian(self, similarity_measure_list):
		return self.louvianClustering(similarity_measure_list)  #One clustering algo
		
	def cluster_ipca(self, similarity_measure_list):
		return self.ipca(similarity_measure_list)  #One clustering algo
	
	def cluster_spectral(self, similarity_measure_list, n_clusters=2):
		return self.spectralClustering(similarity_measure_list, n_clusters)  #Another clustering algo	
