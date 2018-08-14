import os
import sys
import itertools
import glob
import networkx as nx
from networkx.algorithms import isomorphism

def createAllComboList(L,min_len):
	result = []
	for x in range(0, min_len+1):
		for subset in itertools.combinations(L, x):
			result.append(list(subset))
	return result    	

def calcImpNodes(graph):
	imp_nodes=[]
	for x in graph.nodes():
		if( (graph.node[x]['fillcolor']=="#CCCCCC" or graph.node[x]['fillcolor']=="#FFEFD5") and (not "__retres" in graph.node[x]['label'])):
			imp_nodes.append(x)
	return imp_nodes

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
	
#file1_graph, file2_graph = sys.argv[1], sys.argv[2]

file1_graph = "PDG/Correct_A2_corr.main.dot"

pdg_list = glob.glob("PDG/*.main.dot")

graph1 = nx.drawing.nx_agraph.read_dot(file1_graph)
graph1.remove_nodes_from(nx.isolates(graph1)) #Drop Isolates 
imp_nodes_graph1 = calcImpNodes(graph1)
G1 = graph1.subgraph(imp_nodes_graph1)

map_list = []
similarity = []	
for file2_graph in pdg_list:
	if(file1_graph==file2_graph):
		continue
		
	graph2 = nx.drawing.nx_agraph.read_dot(file2_graph)	
	graph2.remove_nodes_from(nx.isolates(graph2)) #Drop Isolates

	imp_nodes_graph2 = calcImpNodes(graph2)
	G2 = graph2.subgraph(imp_nodes_graph2)

	sim,mapping = gammaIso(G1, G2)
	
	similarity.append(sim)
	map_list.append(mapping)

freq_nodes_graph1 = {}
for mapping in map_list:
	for node in list(mapping.iterkeys()):
		try:
			freq_nodes_graph1[node]+=1
		except:
			freq_nodes_graph1[node] = 1
			
sort_freq_nodes_graph1 = sorted(freq_nodes.items(), key=operator.itemgetter(1), reverse=True)	

print sort_freq_nodes_graph1			
