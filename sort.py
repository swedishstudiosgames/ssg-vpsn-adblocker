import platform
p2=["127.0.0.1 ","0.0.0.0 ","||"]
s2=["^"]
i1="input.txt"
o1="output.txt"
l2= set()
f1="\\"if platform.system()=="Windows"else"/"
with open(i1,"r")as f:
    for l1 in f:
        l1=l1.strip()
        for p1 in p2:
            for s1 in s2:
                ml1=p1+l1+s1
                l2.add(ml1)
sl2=sorted(l2)
with open(o1,"w")as f:
    f.write("\n".join(sl2))
