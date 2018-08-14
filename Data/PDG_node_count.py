import networkx as nx
import sys
import glob
import os

def calcImpNodes(graph):
	imp_nodes=[]
	for x in graph.nodes():
		if(graph.node[x]['fillcolor']=="#CCCCCC" or graph.node[x]['fillcolor']=="#FFEFD5" and (not "__retres" in graph.node[x]['label'])):
			imp_nodes.append(x)
	return imp_nodes

folder_path = sys.argv[1]

PDG_path = folder_path+"/PDG"

os.system("mkdir " + PDG_path)

program_files = glob.glob(folder_path+"/Solutions/*.c")

os.system("mkdir " + folder_path + "/Sol_backup/")
os.system("cp -r " + folder_path+"/Solutions/*.c " + folder_path + "/Sol_backup")

for sol in program_files:
	os.system("frama-c -pdg -pdg-dot " + PDG_path + "/" + sol.split("/")[-1].split('.')[0] + " " + sol)

os.system("mkdir " + PDG_path + "/Main")
os.system("mv " + PDG_path + "/*.main.dot " + PDG_path + "/Main/")
os.system("rm " + PDG_path + "/*.*.dot")
os.system("mv " + PDG_path + "/Main/* " +  PDG_path+"/")
os.system("rm -rf " + PDG_path + "/Main")

prog_files_PDG = glob.glob(PDG_path+"/*.dot")

remove_prog_files = []

for pdg in prog_files_PDG:
	graph = nx.drawing.nx_agraph.read_dot(pdg)
	graph.remove_nodes_from(nx.isolates(graph))
	imp_nodes_list = calcImpNodes(graph)
	sub_graph = graph.subgraph(imp_nodes_list)
	if(len(sub_graph.nodes()) <= 15):
		print pdg, len(sub_graph.nodes()) 
	if(len(sub_graph.nodes())>15):
		remove_prog_files.append(pdg.split('/')[-1].split('.')[0] + ".c")

print "Removing Files ....."
print remove_prog_files
for sol in remove_prog_files:
	os.system("rm -rf " + folder_path + "/Solutions/" + sol)
