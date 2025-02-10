# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
       dic = {}
       for each in cpdomains:
        time, domain = each.split()
        n = domain.count('.')
        for i in range(n+1):
            temp = domain.split('.', i)[-1]
            if temp in dic:
                dic[temp] += int(time)
            else:
                dic[temp] = int(time)
       res = []
       for i in dic:
        res.append(f"{dic[i]} {i}")
       return res