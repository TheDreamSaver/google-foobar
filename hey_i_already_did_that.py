l = []
def ternary (n,b):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return ''.join(reversed(nums))

def answer(n,b):
    nlist = map(int,str(n))
    nlist.sort()
    smalllist = map(str,nlist)
    nlist.sort(reverse=True)
    largelist = map(str,nlist)
    small = ''.join(smalllist)
    large = ''.join(largelist)
    n10 = int(large,b) - int(small,b)
    n3 = n10
    if b != 10:
        n3 = ternary(n10,b)
    n3list = list(str(n3))
    if len(n3list) < len(nlist):
        offset = len(nlist) - len(n3list)
        for i in xrange(offset):
            n3list.insert(0,'0')
    n = ''.join(n3list)
    for index,item in enumerate(l):
        if item == n:
            return len(l) - index
    l.append(n)
    return answer(n,b)
