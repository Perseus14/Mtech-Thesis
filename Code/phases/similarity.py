import os
import itertools
import warnings
import networkx as nx
from networkx.algorithms import isomorphism
#import igraph as ig

warnings.filterwarnings("ignore")

CURR_DIR = os.getcwd()
PDG_PATH = CURR_DIR + "/PDG/"
CFG_PATH = CURR_DIR + "/CFG/"

def createAllComboList(L,min_len):
	result = []
	for x in range(0, min_len+1):
		for subset in itertools.combinations(L, x):
			result.append(list(subset))
	return result    	
	
def calcImpNodes(graph):
	imp_nodes=[]
	for x in graph.nodes():
		if((graph.node[x]['fillcolor']=="#CCCCCC" or graph.node[x]['fillcolor']=="#FFEFD5") and (not "__retres" in graph.node[x]['label'])):
			imp_nodes.append(x)
	return imp_nodes
	
class Similarity:
	def __init__(self, ext, graph):
		self.ext1 = ext
		self.ext2 = ext
		if(ext == "mix"): #For Marking Phase check between incoor and corr
			self.ext1 = "_incorr"
			self.ext2 = "_corr"
		self.graph = graph
			
	def gammaIsomorphism(self, file1, file2):	
		def gammaIso(G1, G2):
			
			nm = isomorphism.categorical_node_match(['fillcolor','shape'], ['',''])			
			em = isomorphism.categorical_multiedge_match('color', '')
						
			#G1.remove_nodes_from(nx.isolates(G1)) #Drop Isolates 
			#G2.remove_nodes_from(nx.isolates(G2)) #Drop Isolates
			
			#Create set of induced subgraphs for the Graphs and check for isomorphism.
			len_G1_nodes = len(G1.nodes())
			len_G2_nodes = len(G2.nodes())
			
			min_len = min(len_G1_nodes, len_G2_nodes)
			max_len = max(len_G1_nodes, len_G2_nodes)
			
			G1_list = createAllComboList(G1.nodes(), min_len)
			G2_list = createAllComboList(G2.nodes(), min_len)
			
			induced_subgraph_G1 = [G1.subgraph(node_list) for node_list in G1_list]
			induced_subgraph_G2 = [G2.subgraph(node_list) for node_list in G2_list]	 
			
			new_induced_subgraph_G1 = []
			new_induced_subgraph_G2 = []
			
			#Remove graphs with empty nodes and empty edges			
			for g in induced_subgraph_G1:
				if(len(g.nodes())==0 or len(g.edges())==0):
					continue
				new_induced_subgraph_G1.append(g)
				
			for g in induced_subgraph_G2:
				if(len(g.nodes())==0 or len(g.edges())==0):
					continue
				new_induced_subgraph_G2.append(g)	
				
			induced_subgraph_G1_rev = new_induced_subgraph_G1[::-1]
			induced_subgraph_G2_rev = new_induced_subgraph_G2[::-1]

			similarity = 0
			
			for g1 in induced_subgraph_G1_rev:
				for g2 in induced_subgraph_G2_rev:
					if(len(g1.nodes())==len(g2.nodes()) and len(g1.edges()) == len(g2.edges())):
						GM = isomorphism.MultiDiGraphMatcher(g1,g2,nm,em)
						if(GM.is_isomorphic()):
							similarity = max(similarity, len(g1.nodes())/float(max_len)) 
							return similarity, GM.mapping
			return 0,{}
			
		#genPDG(file1, file2)
		similarityValue = 0
		mapping = {}
		
		file1_PDG = PDG_PATH + file1.split('/')[-1].split('.')[0] + self.ext1 + ".main.dot"
		file2_PDG = PDG_PATH + file2.split('/')[-1].split('.')[0] + self.ext2 + ".main.dot"
		
		file1_CFG = CFG_PATH + file1.split('/')[-1] + self.ext1 + ".dot"
		file2_CFG = CFG_PATH + file2.split('/')[-1] + self.ext2 + ".dot"
		
		if(self.graph=="CFG"):
			file1_graph = file1_CFG
			file2_graph = file2_CFG
			print file1_CFG, file2_CFG
			
		if(self.graph=="PDG"):
			file1_graph = file1_PDG
			file2_graph = file2_PDG
			print file1_PDG, file2_PDG
					
		if(os.path.isfile(file1_graph) and os.path.isfile(file2_graph)): 
			graph1 = nx.drawing.nx_agraph.read_dot(file1_graph)
			#print file1_graph
			graph2 = nx.drawing.nx_agraph.read_dot(file2_graph)
			#print file2_graph
			
			graph1.remove_nodes_from(nx.isolates(graph1)) #Drop Isolates 
			graph2.remove_nodes_from(nx.isolates(graph2)) #Drop Isolates

			#Removing input, returns and other nodes, keeping only the code and declarations from PDG
			imp_nodes_graph1 = calcImpNodes(graph1)
			imp_nodes_graph2 = calcImpNodes(graph2)

			G1 = graph1.subgraph(imp_nodes_graph1)
			G2 = graph2.subgraph(imp_nodes_graph2)

			similarityValue, mapping = gammaIso(G1, G2)
			print similarityValue

		return similarityValue, mapping		

	def getSimilarity(self, file1, file2):
		return self.gammaIsomorphism(file1, file2)	#Call one similarity measure algo
	
	def getSimilarityFromFilesList(self, file_list):
		similarity_measure_list = []
		all_graph_similarity_list = []	#list of list of similarity value, Matrix[graph1][graph2] = similarity
		all_graph_mapping_list = []		#list of list of mappings, Matrix[graph1][graph2] = mapping
		
		#Initialising
		for x in xrange(len(file_list)):
			temp_map = []
			temp_sim = []
			for y in xrange(len(file_list)):
				temp_map.append({}) #Initalise to empty dictionary
				temp_sim.append(0) #Initalise to zero
				
			all_graph_similarity_list.append(temp_sim)
			all_graph_mapping_list.append(temp_map)					
		
		for ind1 in xrange(len(file_list)-1):
			for ind2 in xrange(ind1+1,len(file_list)):
				file1 = file_list[ind1]
				file2 = file_list[ind2]
				sim_val,mapping = self.getSimilarity(file1, file2)
				
				#A[i][j] = A[j][i],  bidirectional!
				
				all_graph_similarity_list[ind1][ind2] = sim_val
				all_graph_similarity_list[ind2][ind1] = sim_val
				
				all_graph_mapping_list[ind1][ind2] = mapping
				all_graph_mapping_list[ind2][ind1] = {val:key for (key, val) in mapping.items()}
				
				similarity_measure_list.append((file1, file2, sim_val))
				
		return similarity_measure_list, all_graph_similarity_list, all_graph_mapping_list  	#List of Tuples(file1, file2, similarity measure)
