class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        D = {}
        for cp in cpdomains:
            l = cp.split(' ')[1].split('.')
            n = len(l)
            for i in range(n):
                ip = '.'.join(l[n-1-i:])
                if ip not in D.keys():
                    D[ip] = int(cp.split(' ')[0])
                else:
                    D[ip] += int(cp.split(' ')[0])
        return ["%s %s"%(D[key], key) for key in D.keys()]