import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP()) # new int
def nl(): return [int(_) for _ in INP().split()] #new line of ints


def check_pref(comp, s1, s2):
    #return true if s2 is prefered over s1
    #print(comp, s1, s2)
    for c in comp:
        if c == s2:
            return True
        if c == s1:
            return False

def solve(pairs, company, student, q):
    #print(pairs)
    #print(company)
    #print(student)
    #print(q)
    applicants = [-1 for _ in range(pairs+1)]
    
    while q:
        s = q.pop(0)
        #print(student)
        ranking,  apply_idx = student[s]
        pref_comp = ranking[apply_idx]

        curr_applicant = applicants[pref_comp]
        #no previous applicants
        if applicants[pref_comp] == -1:
            applicants[pref_comp] = s

        elif check_pref(company[pref_comp], curr_applicant, s):
            q.append(applicants[pref_comp])
            applicants[pref_comp] = s

        else:
            q.append(s)
        student[s][1] += 1

    print('\n'.join(map(str,applicants[1:])))



pairs = ni()
#note that problem is 1 idexed
#using array as they are faster than dict
#structure arr[id] = [[preferences], current application id]
company = [[] for _ in range(pairs+1)]
student = [[]for _ in range(pairs+1)]
student_ids = []

seen = {}
for case in range(2*pairs):
    row = nl()
    id = row[0]
    if id in seen:
        student[id] = [row[1:], 0]
        student_ids.append(id)
    else:
        company[id] = row[1:]
        seen[id] = True


solve(pairs,company, student, student_ids)