from math import sqrt
def isp(n):
    if n == 2 or n == 3:
        return True
    if n%6!=1 and n%6!=5:
        return False
    tmp = sqrt(n)
    for i in xrange(5,int(tmp)+1,6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

def idnum(index):
    start = 2
    pnum = 0
    idstr = ''
    while True:
        if isp(start):
            if pnum > index + 5:
                return idstr[index:index+5]
            idstr += str(start)
            pnum += 1
        start += 1
