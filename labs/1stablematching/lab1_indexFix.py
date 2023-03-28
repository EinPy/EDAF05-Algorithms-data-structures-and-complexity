import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP()) # new int
def nl(): return [int(_) for _ in INP().split()] #new line of ints


def check_pref(comp, s1, s2):
    # return True if s2 is preferred over s1
    for c in comp:
        if c == s2:
            return True
        elif c == s1:
            return False
    # s1 is not in the preference list, so s2 is preferred
    return True

def solve(pairs, company, student, q):
    applicants = [-1 for _ in range(pairs)]
    while q:
        s = q.pop(0)
        ranking, apply_idx = student[s]
        pref_comp = ranking[apply_idx]

        curr_applicant = applicants[pref_comp]
        if curr_applicant == -1:
            applicants[pref_comp] = s
            student[s][1] += 1 # only update index if assigned
        elif check_pref(company[pref_comp], curr_applicant, s):
            q.append(applicants[pref_comp])
            applicants[pref_comp] = s
            student[s][1] += 1 # only update index if assigned
        else:
            q.append(s)
            student[s][1] += 1
    print('\n'.join(map(str,[x+1 for x in applicants])))


pairs = ni()
#using list as they are faster than dict
#structure arr[id] = [[preferences], current application id]
company = [[] for _ in range(pairs)]
student = [[]for _ in range(pairs)]
student_ids = []

seen = {}
for case in range(2*pairs):
    row = nl()
    id = row[0] - 1 # adjust index to 0-based
    if id in seen:
        student[id] = [[x -1 for x in row[1:]], 0]
        student_ids.append(id)
    else:
        company[id] = [x-1 for x in row[1:]] # adjust index to 0-based
        seen[id] = True


solve(pairs, company, student, student_ids)
