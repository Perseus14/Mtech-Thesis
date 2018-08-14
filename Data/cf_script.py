import urllib
import json
import time, os

MAX_SUBS = 1000000
MAX_CF_CONTEST_ID = 600
MAGIC_START_POINT = 17000

parent_dir='CodeForces'

CONTEST_STATUS = 'http://codeforces.com/api/contest.status?contestId={ContestId}&from=1&count=10000'
LANG = ['GNU C', 'GNU C11'] #[ 'GNU C++14', 'GNU C++11', 'GNU C++']
SUBMISSION_URL = 'http://codeforces.com/contest/{ContestId}/submission/{SubmissionId}'
                          
SOURCE_CODE_BEGIN_cpp = '<pre class="prettyprint lang-cpp program-source" style="padding: 0.5em;">'
#SOURCE_CODE_BEGIN_c = '<pre class="prettyprint lang-c program-source" style="padding: 0.5em;">'

SOURCE_CODE_BEGIN_c = '<pre id="program-source-text" class="prettyprint lang-c program-source" style="padding: 0.5em;">'

EXT = {'C++': 'cpp', 'C': 'c'}
EXT_keys = EXT.keys()

replacer = {'&quot;': '\"', '&gt;': '>', '&lt;': '<', '&amp;': '&', "&apos;": "'", "&#39;": '\''}
keys = replacer.keys()

def get_ext(comp_lang):
    if 'C++' in comp_lang:
        return 'cpp'
    for key in EXT_keys:
        if key in comp_lang:
            return EXT[key]
    return ""

def parse(source_code):
    for key in keys:
        source_code = source_code.replace(key, replacer[key])
    return source_code

if not os.path.exists(parent_dir):
    os.makedirs(parent_dir)


contest_id = int(raw_input('Enter Contest ID: '))
problem_id = raw_input('Enter Problem ID: ')
contest_status = urllib.urlopen(CONTEST_STATUS.format(ContestId=contest_id)).read()
dic = json.loads(contest_status)
if dic['status'] != u'OK':
    print 'Oops.. Something went wrong...'
    exit(0)

submissions = dic['result']
start_time = time.time()

soln_id_c = 0
soln_id_ic = 0
flag = True
for submission in submissions:
    if( (submission['verdict'] == u'OK' or submission['verdict'] == u'WRONG_ANSWER') and (submission['programmingLanguage'] in LANG) and (submission['problem']['index'] == problem_id)):
        con_id, sub_id = submission['contestId'], submission['id'],
        prob_name, prob_id = submission['problem']['name'], submission['problem']['index']
        comp_lang = submission['programmingLanguage']
        print comp_lang
        while(flag):
            try:
               submission_info = urllib.urlopen(SUBMISSION_URL.format(ContestId=con_id, SubmissionId=sub_id)).read()
               flag = False
            except:
               flag = True
        flag = True
        if(comp_lang == 'GNU C' or comp_lang == 'GNU C11' ): 
            start_pos = submission_info.find(SOURCE_CODE_BEGIN_c, MAGIC_START_POINT) + len(SOURCE_CODE_BEGIN_c)
        else:
            start_pos = submission_info.find(SOURCE_CODE_BEGIN_cpp, MAGIC_START_POINT) + len(SOURCE_CODE_BEGIN_cpp)
        end_pos = submission_info.find("</pre>", start_pos)
        result = parse(submission_info[start_pos:end_pos]).replace('\r', '')
        ext = get_ext(comp_lang)
        new_directory = parent_dir + '/' + str(con_id) + '/Solutions'
        if(submission['verdict'] == u'OK'):
            status = "Correct"
            soln_id_c+=1
            soln_id = soln_id_c
        else:
       	    status = "Incorrect"
            soln_id_ic+=1
            soln_id = soln_id_ic 
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        filename = new_directory + '/' + status + "_" +prob_id + str(soln_id) +'.' + ext 
        file = open(filename, 'w')
        file.write(result)
        file.close()
        print filename		

end_time = time.time()
print 'Execution time %d seconds' % int(end_time - start_time)
