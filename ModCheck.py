from copy import deepcopy as dp
import sys
import time
class PropRepr():
    def KB(self,kb1):
        k1= dp(kb1)
        ja = k1[0:k1.index("|=")]
        jb = k1[k1.index("|=")+2:]
        sym =self.symbols(ja.split(" "),jb.split(" "))
        return ja,jb,sym
    def symbols(self,ja1,jb1):
        ja2 = dp(ja1)
        jb2 = dp(jb1)
        sm =[]
        for a1 in ja2:
            if a1 not in {",","^","v","->","<>","!"," ",'',"|="}:
                sm.append(a1)
        for b1 in jb2:
            if b1 not in {",","^","v","->","<>","!"," ",'',"|="}:
                sm.append(b1)
        return list(set(sm))
    def KB_conv(self,kb2,dict1):
        d1 = dp(dict1)
        k2 =dp(kb2)
        if len(k2.split())>3:
            if "<>" in k2.split():
                l = k2.split("<>")
                return self.comp(self.KB_conv(l[0],d1),self.KB_conv(l[1],d1),"<>")
            if "->" in k2.split():
                l = k2.split("->")
                return self.comp(self.KB_conv(l[0],d1),self.KB_conv(l[1],d1),"->")
            if "^" in k2.split():
                l = k2.split("^",1)
                return self.comp(self.KB_conv(l[0],d1),self.KB_conv(l[1],d1),"^")
            if "v" in k2.split():
                l = k2.split("v",1)
                return self.comp(self.KB_conv(l[0],d1),self.KB_conv(l[1],d1),"v")
        else:
            k3 = k2.split()
            if len(k3) ==3:
                return self.comp(d1[k3[0]],d1[k3[2]],k3[1])
            elif len(k3) == 2:
                return (not d1[k3[1]])
            elif len(k3) == 1:
                return d1[k3[0]]
            else:
                print("Error: empty clause", file= sys.stderr)
    def comp(self,l1,l2,s1):
        if s1 =="v":
            return (l1 | l2)
        elif s1 == "->":
            if l1:
                return l2
            else:
                return True
        elif s1 == "<>":
            if l1==l2:
                return True
            else:
                return False
        elif s1 == "^":
            return (l1 & l2)
        else:
            print("Invalid symbol encountered",s1,"\t" , file=sys.stderr)
    def ttval (self,n):
        if n < 1:
            return [[]]
        tt2 = self.ttval(n-1)
        return [ i + [j] for i in tt2 for j in [True,False] ]
    def TTCheck(self,kb3,al3,sym1):
        kb4=dp(kb3)
        al4=dp(al3)
        sym4 = dp(sym1)
        l = self.ttval(len(sym4))
        d={}
        mod = []
        kl=1
        for i in l:
            for m in range(len(i)):
                d[sym4[m]]=i[m]
            t1 = True
            t2 = True
            for i1 in kb4.split(","):
                t1 = t1 & self.KB_conv(i1,d)
            for i2 in al4.split(","):
                t2 = t2 & self.KB_conv(i2,d)
            if t1:
                if not t2:
                    kl=0
                    break
                else:
                    l=dp(d)
                    mod.append(l)
        if kl==0:
            print(al4, "cannot be inferred")
        else:
            print(al4, " can be inferred")
            i=0
            for j in mod:
                print("Model",i+1,":",j,file=sys.stderr)
                i +=1
p1=PropRepr()
inp = 'y'
while inp== 'y' or inp =='Y':
    ps = input("Enter the Proposition Sentence to be tested \t ")
    st = time.perf_counter()
    alp,beta,sym=p1.KB(ps)
    p1.TTCheck(alp,beta,sym)
    print("Time taken = ",(time.perf_counter()-st),"s",file = sys.stderr)
    inp = input("Enter y to check another sentance or n to exit \t ")

# Problems
    
#1. 
# P , P -> Q |= Q
# P , P -> Q |= ! Q

#2. 
# ! P11 , B11 <> P12 v P21 , B21 <> P11 v P22 v P31 , ! B11 , B21 |= P12
# ! P11 , B11 <> P12 v P21 , B21 <> P11 v P22 v P31 , ! B11 , B21 |= ! P12

#3.
# Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= Mythical
# Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= ! Mythical
# Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= Magical
# Mythical -> ! Mortal , ! Mythical -> Mortal ^ Mammal , ! Mortal v Mammal -> Horned , Horned -> Magical |= Horned

#4.a 
# Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= Amy
# Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= ! Amy
# Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= Bob
# Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= ! Bob
# Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= Cal
# Amy <> Cal ^ Amy , Bob <> ! Cal , Cal <> Bob v ! Amy |= ! Cal

#4.b
# Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= Amy
# Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= ! Amy
# Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= Bob
# Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= ! Bob
# Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= Cal
# Amy <> ! Cal , Bob <> Amy ^ Cal , Cal <> Bob |= ! Cal
