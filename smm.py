import random 


while True:
    ls = random.sample(range(0,10), 10)
    ls.remove(1)
    ls = [str(x) for x in ls]
    s = ls[0];e = ls[1];n = ls[2];d = ls[3]
    m = '1' ;o= ls[4];r = ls[5];y = ls[6]
    sasi = s+e+n+d
    vatsal = m+o+r+e
    ans = m+o+n+e+y
    summ = int(sasi)+int(vatsal)
    if summ == int(ans):
        print(sasi,vatsal,ans)
        break
    else:
        print(sasi,vatsal,ans)
        continue
