# Mtech Thesis
Code for my Mtech  thesis, Automated Evaluation of Programming Assignments.

## Installation

apt install frama-c  
pip install -r requirements.txt

## Data Preparation

+ Data/
  + <folder_name>
     + Solutions/  
         + Solution1.c  
         + Solution2.c  
             .  
             .  
             .  
     + reference.c
     + clustering.csv  
     + grading.csv  
 
### Explanation
  + *Solutions*  folder contains all the student solutions
  + reference.c is the professors solutions 
  + clustering.csv contains the cluster to which each solution belongs to, assigned by a rater(optional, only for verifying results)  
  + grading.csv contains the grades for each solution, assigned by a rater (optional, only for verifying results)
## Execution

python eval.py <folder_path> --noeval   

### Usage
python eval.py -h for other parameters  

## Examples

In example folder, there are saved ipython workplace to verify results.   
 
To use, in linux terminal, type ipython, then   

import dill  
dill.load(<filename>)  
  
  
