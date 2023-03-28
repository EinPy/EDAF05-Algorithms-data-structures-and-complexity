import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP()) # new int
def nl(): return [int(_) for _ in INP().split()] #new line of ints


def check_pref(comp, s1, s2):
    #return true if s2 is prefered over s1
    for c in comp:
        if c == s2:
            return True
        else:
            return False

def solve(pairs, company, student):
    q = [i for i in range(1,pairs+1)] #0 indexed queue of students
    applicants = [False for _ in range(pairs+1)]
    
    while q:
        s = q.pop(0)
        apply_idx = student[s][1]
        pref_comp = student[s][0][apply_idx]

        if applicants[pref_comp] == False: #potential bug confusing 0 and False
            applicants[pref_comp] = s

        elif check_pref(company[pref_comp], student[applicants[pref_comp]][0], student[s][0]):
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

seen = {}
for case in range(2*pairs):
    row = nl()
    id = row[0]
    if id in seen:
        student[id] = [row[1:], 0] 
    else:
        company[id] = [row[1:], 0]
        seen[id] = True


solve(pairs,company, student)