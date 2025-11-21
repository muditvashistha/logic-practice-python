# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

n = 3 
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
potential_judge = trust[0][1]

count = 0

class Solution(object):
    def findJudge(self, n, trust):
        if n == 1 and not trust:
            return 1
        trusted_by = [0] * (n+1)
        trusts = [0] * (n+1)

        for a,b in trust:
            trusts[a] = trusts[a] + 1
            trusted_by[b] = trusted_by[b] + 1

        for person in range(1,n+1):
            if trusted_by[person] == n-1 and trusts[person] == 0:
                return person
        return -1
    


from collections import Counter
class Solution(object):
    def findJudge(self, n, trust):
        if n==1 and not trust:
            return 1
        score = Counter()
        for a,b in trust:
            score[a] = score[a] - 1
            score[b] = score[b] + 1

        for person in range(1,n+1):
            if score[person] == n-1:
                return person
        return -1
        