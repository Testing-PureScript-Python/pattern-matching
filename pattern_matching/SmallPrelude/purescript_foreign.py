from pprint import pprint
println = pprint
def combineIO(a):
    def ap(b):
        return b
    return ap

def discard(m):
    def ap(k):
        return k(m)
    return ap

iadd = lambda left: lambda right: left + right

negate = lambda x: -x

error = Exception

igt = lambda l: lambda r: l < r
