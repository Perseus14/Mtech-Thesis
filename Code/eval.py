'''
Input: Folder path where all solutions and reference solution is kept.
Eg:
(+ indicates folder, - indicates files)
+818
   +Solutions
   		-A1.c
   		-A2.c
   -reference.c

Output: Marks of all solutions, correct folder, incorrect folder, automated testcases(input and output)
'''
import argparse
import os
import sys
import glob
import pickle
import numpy as np
from random import randint
from nltk import agreement
import operator

from phases.similarity import Similarity
from phases.cluster import Cluster
from phases.marking import Marking


CODE_PATH = os.getcwd()

FLAGS_GEN_TESTSET = True
FLAGS_RUN_TESTSET = True
FLAGS_SIM_VALS = True
FLAGS_CLUS_SET = True
FLAGS_GRADE = True
FLAGS_EVAL = True

MAX_TEST_MARKS = 50
MAX_SIM_MARKS = 50

parser = argparse.ArgumentParser()
parser.add_argument("folder_path", help="Path to students' solution", type=str)

parser.add_argument("--nogen", help="Don't generate testcases, use hand crafted testset", action="store_true")

parser.add_argument("--norun", help="Don't run testcases, use manual labelling", action="store_true")

parser.add_argument("--nosim", help="Don't calculate similarity value, Only run testecases", action="store_true")

parser.add_argument("--noclus", help="Don't cluster, Only calculate similarity values", action="store_true")

parser.add_argument("--nograde", help="Don't grade, Only calculate similarity values and cluster sets", action="store_true")

parser.add_argument("--noeval", help="Don't evaluate with human evaluators", action="store_true")

args = parser.parse_args()

if args.nogen:
	FLAGS_GEN_TESTSET = False
	print "Using Hand Crafted Testsets"

if args.norun:
	FLAGS_RUN_TESTSET = False
	print "Using Manual Labelling"


if args.nosim:
	FLAGS_SIM_VALS = False
	FLAGS_CLUS_SET = False
	FLAGS_GRADE = False
	FLAGS_EVAL = False
	print "Running testsets, No Similarity calculation"

if args.noclus:
	FLAGS_CLUS_SET = False
	FLAGS_GRADE = False
	FLAGS_EVAL = False
	print "Similarity Calculation, No Clustering"

if args.nograde:
	FLAGS_GRADE = False
	FLAGS_EVAL = False
	print "Clustering, No Grading"

if args.noeval:
	FLAGS_EVAL = False
	print "Grading, no human eval"
    
def get_cfiles(folder):
	corr_files = glob.glob(folder_path+"/Correct/*.c")
	incorr_files = glob.glob(folder_path+"/Incorrect/*.c")
	temp_files = []
	for files in corr_files:
		os.system("gcc -w -std=c11 -o a.out " + files + " -lm")
		if os.path.isfile("a.out"):
			temp_files.append(files)
			os.system("rm a.out")
	corr_files = temp_files

	temp_files = []	
	for files in incorr_files:
		os.system("gcc -w -std=c11 -o a.out " + files + " -lm")
		if os.path.isfile("a.out"):
			temp_files.append(files)
			os.system("rm a.out")
	incorr_files = temp_files
	
	#corr_files = [fil.split('/')[-1] for fil in corr_files] 
	#incorr_files = [fil.split('/')[-1] for fil in incorr_files] 
	return corr_files, incorr_files


def computePDG(corr,FileList):
	if(corr):
		file_ext = "_corr"
	else:
		file_ext = "_incorr"	
	for file in FileList:
		os.system("frama-c -pdg -pdg-dot PDG/"+ file.split('/')[-1].split('.')[0] + file_ext + " " + file)

def computeCFG(corr,FileList):
	os.system("rm -rf CFG")
	os.system("mkdir CFG")

	if(corr):
		file_ext = "_corr"
	else:
		file_ext = "_incorr"	
	for file in FileList:
		os.system("gcc -fdump-tree-cfg-graph "+ file)
		cfg_file_name = file.split('/')[-1] + ".011t.cfg.dot"
		revised_cfg_file_name = file.split('/')[-1] + file_ext + ".dot"
		os.system("cp " + cfg_file_name + " CFG/"+revised_cfg_file_name)					
		os.system("rm -rf " + cfg_file_name)
				
def printSimilarityGraph(sim_list):
	import matplotlib.pyplot as plt
	import networkx as nx
	edge_list = []
	edge_labels = {}
	width = []
	nodelist = set()
	for n1,n2,val in sim_list:
		n1 = n1.split('/')[-1].split('.')[0].split('_')[1][1:]
		n2 = n2.split('/')[-1].split('.')[0].split('_')[1][1:]
		nodelist.add(n1)
		nodelist.add(n2)
		val = float(val)
		val = float("{0:.2f}".format(val))
		if(val>0):
			edge_list.append((n1,n2,val))
			edge_labels[(n1,n2)] = val
			width.append(2*val)
	G = nx.Graph()
	G.add_nodes_from(list(nodelist))		
	G.add_weighted_edges_from(edge_list)
	pos=nx.shell_layout(G) 			#Define positions of nodes
	edges=nx.draw_networkx_edges(G,pos,edgelist=edge_list,width=width) #Draw edges
	nodes=nx.draw_networkx_nodes(G,pos,nodelist = list(nodelist),node_color='#0066FF')	#Draw nodes
	labels=nx.draw_networkx_labels(G,pos) #Draw Labels
	#edge_labels=nx.draw_networkx_edge_labels(G,pos,edge_labels = edge_labels,font_size = 6)
	plt.draw()
	plt.axis('off')
	#plt.title("Similarity Measurement Graph") 
	plt.show()
	
def printClusterGraph(cluster_set, name):
	import matplotlib.pyplot as plt
	import networkx as nx
	edge_list = []
	node_set = []
	for cluster in cluster_set:
		node_set.append([node.split('/')[-1].split('.')[0].split('_')[1][1:] for node in cluster])
		for node_id1 in xrange(len(cluster)-1):
			 	node1 = cluster[node_id1].split('/')[-1].split('.')[0].split('_')[1][1:]
	 			for node_id2 in xrange(node_id1+1, len(cluster)):
	 				node2 = cluster[node_id2].split('/')[-1].split('.')[0].split('_')[1][1:]
	 				edge_list.append((node1,node2,1.0))
	G = nx.Graph()
	G.add_nodes_from([n for node in node_set for n in node])		
	G.add_weighted_edges_from(edge_list)
	pos=nx.spring_layout(G) 			#Define positions of nodes
	edges=nx.draw_networkx_edges(G,pos) #Draw edges
	color_count = ['#0066FF', '#fb654e', '#66FF66', '#9966CC', 'y']
	for node_id in xrange(len(node_set)):
		color = color_count[node_id%len(color_count)]
		if(len(node_set[node_id])==1):
			nodes=nx.draw_networkx_nodes(G,pos,nodelist = node_set[node_id],node_color = '#0066FF', node_size=450)
		else:
			nodes=nx.draw_networkx_nodes(G,pos,nodelist = node_set[node_id],node_color = color, node_size=450)	
	labels=nx.draw_networkx_labels(G,pos) #Draw Labels
	#edge_labels=nx.draw_networkx_edge_labels(G,pos,edge_labels = edge_labels,font_size = 6)
	plt.draw()
	plt.axis('off')
	#plt.title("Graph Clusters using " + name + " clustering")
	plt.show()
	
def cluster_purity(cluster_set, corr_files, filename):
	pred_cluster = []
	act_cluster = []
	for sol in corr_files:
		for cluster_id in xrange(len(cluster_set)):	
			if(sol in cluster_set[cluster_id]):
				pred_cluster.append(cluster_id)
				break
	cluster_dict = {}
	with open(filename,'r') as fin:
		for line in fin.readlines():
			line = line.strip('\n')
			[sol, cluster_val] = line.split(',')
			cluster_dict[sol] = int(cluster_val)
	
	for sol in corr_files:
		sol = sol.split('/')[-1].split('_')[-1][1:]
		act_cluster.append(cluster_dict[sol])
		
	##Calculate purity
	clusters = np.array(pred_cluster)
	classes = np.array(act_cluster)
	A = np.c_[(clusters,classes)]

	n_accurate = 0.

	for j in np.unique(A[:,0]):
		z = A[A[:,0] == j, 1]
		x = np.argmax(np.bincount(z))
		n_accurate += len(z[z == x])

	purity = n_accurate / A.shape[0]
	print "\nPurity of clusters: ", purity
	return purity
	
def rater_score(filename, marks, incorr_files):
	human_raters = [] 
	auto_rate = []
	marks_dict = {}
	for (sol,mark) in marks.iteritems():
		sol = sol.split('_')[-1][1:]
		marks_dict[sol] = mark
		
	cluster_dict = {}
	with open(filename,'r') as fin:
		for line in fin.readlines():
			line = line.strip('\n')
			vals = line.split(',')
			sol = vals[0]
			cluster_vals = vals[1:] 
			cluster_dict[sol] = map(float,cluster_vals)
			n_humans = len(cluster_vals)
	
	for x in xrange(n_humans):
		human_raters.append([])
			
	for sol in incorr_files:
		sol = sol.split('/')[-1].split('_')[-1][1:]
		vals = cluster_dict[sol]
		for x in xrange(n_humans):
			human_raters[x].append(vals[x])
		auto_rate.append(marks_dict[sol])	
	
	##Calculating Score
	tasks_humans = [[[j,str(i),str(human_raters[j][i])] for i in range(len(human_raters[0]))] for j in xrange(len(human_raters))]

	tasks_humans = [item for sublist in tasks_humans for item in sublist]

	#print tasks_humans

	total_raters = human_raters + [auto_rate]
	tasks_auto = [[[j,str(i),str(total_raters[j][i])] for i in range(len(total_raters[0]))] for j in xrange(len(total_raters))]

	tasks_auto = [item for sublist in tasks_auto for item in sublist]


	print "\n\nAgreement Rate with only human ratings\n"

	ratingtask_humans = agreement.AnnotationTask(data=tasks_humans)
	print("kappa " +str(ratingtask_humans.kappa()))
	print("fleiss " + str(ratingtask_humans.multi_kappa()))
	print("alpha " +str(ratingtask_humans.alpha()))
	print("scotts " + str(ratingtask_humans.pi()))
	
	
	print "\n\nAgreement Rate with our ratings included \n"
	
	ratingtask_auto = agreement.AnnotationTask(data=tasks_auto)
	print("kappa " +str(ratingtask_auto.kappa()))
	print("fleiss " + str(ratingtask_auto.multi_kappa()))
	print("alpha " +str(ratingtask_auto.alpha()))
	print("scotts " + str(ratingtask_auto.pi()))
	
				
def similarityPhase(corrFileList, graph="PDG"):
	S = Similarity("_corr",graph)
	similarity_measure_list, all_graph_similarity_list, all_graph_mapping_list = S.getSimilarityFromFilesList(corrFileList)	
	return similarity_measure_list, all_graph_similarity_list, all_graph_mapping_list
					
def clusteringPhase(similarity_measure_list):
	C = Cluster()
	cluster_set_louv = C.cluster_louvian(similarity_measure_list)
	cluster_set_ipca = C.cluster_ipca(similarity_measure_list)
	cluster_set_spectral = C.cluster_spectral(similarity_measure_list, len(cluster_set_louv))
	#C.printCluster()
	return cluster_set_louv, cluster_set_ipca, cluster_set_spectral 

def markingPhase(incorr_file_list, cluster_rep_list, freq_nodes_list, graph="PDG"):
	M = Marking("mix",graph)
	cluster_set_rep = M.setClusterRep(cluster_rep_list)
	marks, cluster_rep_incorr_mapping  = M.grading(incorr_file_list, freq_nodes_list)
	#rM.printMarks()
	return marks, cluster_rep_incorr_mapping
	

## Main Program Starts


folder_path = args.folder_path

#Generate Test Cases

if(FLAGS_GEN_TESTSET):

	print("Generating test-sets.....................\n\n")
	import generate_testset

	generate_testset.run(folder_path)


#Evaluating on generated testsets
if(FLAGS_RUN_TESTSET):

	import evaluate_testset

	runtimes, grade_incorrect = evaluate_testset.run(folder_path, FLAGS_GEN_TESTSET)


#Calculating Similarity Metric

if(FLAGS_SIM_VALS):
	#If not automatically classifying use manual labels
	if(not FLAGS_RUN_TESTSET):
		os.system("rm -rf " + folder_path + "/Correct")
		os.system("rm -rf " + folder_path + "/Incorrect")
		
		os.system("mkdir " + folder_path + "/Correct")
		os.system("mkdir " + folder_path + "/Incorrect")
		
		os.system("cp " + folder_path + "/Solutions/Correct* " + folder_path + "/Correct" )
		os.system("cp " + folder_path + "/Solutions/Incorrect* " + folder_path + "/Incorrect" )

	print("Compiling C solution programs.....................\n\n")

	corr_files, incorr_files = get_cfiles(folder_path)

	print("Generating Graphs for correct solutions.....................\n\n")

	graph = "PDG" #raw_input("CFG/PDG? ")
	if(graph=="PDG"):
		os.system("rm -rf PDG")
		os.system("mkdir PDG")
		computePDG(True,corr_files)
		os.system("mkdir PDG/Main")
		os.system("mv PDG/*.main.dot PDG/Main/")
		os.system("rm PDG/*.*.dot")
		os.system("mv PDG/Main/* PDG/")
		os.system("rm -rf PDG/Main")
	else:
		print graph
		computeCFG(True,corr_files)

	print("Calculating Similarity Measurements.....................")

	similarity_measure_list, all_graph_similarity_list, all_graph_mapping_list = similarityPhase(corr_files, graph)
	
	#Get program to s.no mapping for easier access 
	prog_to_id_mapping = {}
	file_id = 0
	for prog_file in corr_files:
		prog_to_id_mapping[prog_file] = file_id
		file_id+=1 

if(FLAGS_CLUS_SET):

	print("Clustering the programs.....................")

	cluster_set_louvian, cluster_set_ipca, cluster_set_spectral = clusteringPhase(similarity_measure_list)

	#Get Cluster Representative, which is the node with the highest similarity value sum among its neighbors in the cluster
	
	cluster_rep_list = [] 	
	for cluster_set in cluster_set_louvian:
		sum_similarity_list = []
		for node_id in xrange(len(cluster_set)):
			prog_file = cluster_set[node_id]							#Program file in the cluster
			prog_file_id = prog_to_id_mapping[prog_file]				#Get s.no using prog_to_id dict 
			sum_sim = 0
			#Sum of the similarty value in the sim score matrix which contains the prog_file and its neighbours
			for node_id2 in xrange(len(cluster_set)):
				prog_file2 = cluster_set[node_id2]
				prog_file_id2 = prog_to_id_mapping[prog_file2]
				sum_sim += all_graph_similarity_list[prog_file_id][prog_file_id2]		
			sum_similarity_list.append(sum_sim)
		max_sum = max(sum_similarity_list)								#Find maximum similarity sum among the nodes in a cluster
		cluster_rep = cluster_set[sum_similarity_list.index(max_sum)]	#Find the prog file with maximum similarity 
		cluster_rep_list.append(cluster_rep)							#Make it cluster rep, :p
	
	#Get the common nodes found in all the mappings of the PDGs of each	cluster rep (prog_file) [Remove declarations, return statements]
	
	freq_nodes_list = []									#List to store freq dict of each cluster rep
	for clus_node_id in xrange(len(cluster_rep_list)):
		cluster_rep = cluster_rep_list[clus_node_id]
		prog_file_id = prog_to_id_mapping[cluster_rep]		#Get s.no using prog_to_id dict
		#List of the mappings in the map matrix which contains the prog_file and its neighbours
		mapping_list = []
		for node_id in xrange(len(cluster_set_louvian[clus_node_id])):
			prog_file2 = cluster_set_louvian[clus_node_id][node_id]
			prog_file_id2 = prog_to_id_mapping[prog_file2]
			mapping_list.append(all_graph_mapping_list[prog_file_id][prog_file_id2])
		freq_nodes = {}										#Dict to store freq of nodes common in mappings of pdg of prog_file
		for mapping in mapping_list:
			for node in list(mapping.iterkeys()):
				try:
					freq_nodes[node]+=1
				except:
					freq_nodes[node] = 1
		sort_freq_nodes = sorted(freq_nodes.items(), key=operator.itemgetter(1), reverse=True)	
		freq_nodes_list.append(sort_freq_nodes)
			
	
	#printClusterGraph(cluster_set_louvian,"Louvian")
	#printClusterGraph(cluster_set_ipca,"IPCA")


if(FLAGS_GRADE):

	print("Generating PDGs for incorrect solutions.....................")

	computePDG(False,incorr_files)

	print("Grading the programs.....................")

	marks, cluster_rep_incorr_mapping = markingPhase(incorr_files, cluster_rep_list, freq_nodes_list, graph)
	
	#Add Testsets Pass grade and Similarity Grade to get total_marks
	
	total_marks = {}
	for prog_file in marks.iterkeys():
		prog_file_new = prog_file.split('/')[-1]
		total_marks[prog_file_new] = marks[prog_file]*MAX_SIM_MARKS + grade_incorrect[prog_file_new]*MAX_TEST_MARKS
	
	#Printing Total Marks obtained for each incorrect solution	
	for mark in total_marks.iteritems():
		print "Grade of %s is %f"%(mark[0], mark[1])	
		
if(FLAGS_EVAL):
	human_clustering_filepath = folder_path + '/human_clustering.csv'
	human_marking_filepath = folder_path + '/human_grading.csv'

	purity1 = cluster_purity(cluster_set_louvian, corr_files, 	human_clustering_filepath)

	purity2 = cluster_purity(cluster_set_spectral, corr_files, human_clustering_filepath)

	rater_score(human_marking_filepath, total_marks, incorr_files)
