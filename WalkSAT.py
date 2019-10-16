from copy import deepcopy as dp
import random
import sys
import time
class PropRepr():
    def kb(self,kb1):
        k1= dp(kb1)
        if " |= " in k1:
            k1 = k1.replace("|=",",")
        return k1.split(","),self.symbols(k1.split(" "))
    def symbols(self,k12):
        k2 = dp(k12)
        sm =[]
        for a1 in k2:
            if a1 not in {"^","v","->","<>","!"," ",'',"|=",","}:
                sm.append(a1)
        return list(set(sm))
    def kb_conv(self,kb2,dict1):
        d1 = dp(dict1)
        k2 =dp(kb2)
        if len(k2.split())>3:
            if "<>" in k2.split():
                l = k2.split("<>")
                return self.comp(self.kb_conv(l[0],d1),self.kb_conv(l[1],d1),"<>")
            if "->" in k2.split():
                l = k2.split("->")
                return self.comp(self.kb_conv(l[0],d1),self.kb_conv(l[1],d1),"->")
            if "^" in k2.split():
                l = k2.split("^",1)
                return self.comp(self.kb_conv(l[0],d1),self.kb_conv(l[1],d1),"^")
            if "v" in k2.split():
                l = k2.split("v",1)
                return self.comp(self.kb_conv(l[0],d1),self.kb_conv(l[1],d1),"v")
        else:
            k3 = k2.split()
            if len(k3) ==3:
                return self.comp(d1[k3[0]],d1[k3[2]],k3[1])
            elif len(k3) == 2:
                return (not d1[k3[1]])
            elif len(k3) == 1:
                return d1[k3[0]]
            else:
                print("Error empty clause" , file=sys.stderr)
    def comp(self,l1,l2,s1):
        if s1 =="v":
            return (l1 or l2)
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
            print("Invalid symbol encountered",s1,"\t",file=sys.stderr)
class WalkSAT(PropRepr):
    def wSAT(self, k13,sym1, p=0.5, max_flips=10000):
        k4=dp(k13)
        d = dict([(s, random.choice([True, False])) for s in sym1])
        for i in range(max_flips):
            satisfied, unsatisfied = [], []
            for a1 in k4:
                if self.kb_conv(a1,d):
                    satisfied.append(a1)
                else:
                    unsatisfied.append(a1)
            if not unsatisfied:
                print("Satisfiable")
                print("Model = ", d , file=sys.stderr)
                return
            a1 = random.choice(unsatisfied)
            if random.random()> p:
                sym2 = random.choice(self.symbols(a1.split(" ")))
            else:
                sym11 = []
                l = []
                for i in self.symbols(a1.split(" ")):
                    sym11.append(i)
                sym11 = list(set(sym11))
                for i in range(len(sym11)):
                    j = 0
                    d1 = dp(d)
                    d1[sym11[i]] = not d1[sym11[i]]
                    for a2 in k4:
                        if self.kb_conv(a2,d1):
                            j += 1
                    l.append(j)
                sym2 = sym11[l.index(max(l))]
            d[sym2] = not d[sym2]
        print("Unsatisfiable")
p1=WalkSAT()
k=1
while k == 1:
    ps = input("Enter the Proposition Sentence to be tested \t ")
    st = time.perf_counter()
    cl,symb =p1.kb(ps)
    p1.wSAT(cl,symb)
    print("Time taken = ",(time.perf_counter()-st),"s",file = sys.stderr)
    Sw =input(" Do  you want to check any more sentences (Y/N) \t")
    if Sw == 'Y' or Sw == 'y':
        k=1
    else:
        k=0
        
# Problems

#1.
# P , ! P v Q |= Q
# P , ! P v Q |= ! Q

#2.
# ! P11 , ! B11 v P12 v P21 ^ ! P12 v B11 ^ ! P21 v B11 , ! B21 v P11 v P22 v P31 ^ ! P11 v B21 ^ ! P22 v B21 ^ ! P31 v B21 , ! B11 , B21 |= P12
# ! P11 , ! B11 v P12 v P21 ^ ! P12 v B11 ^ ! P21 v B11 , ! B21 v P11 v P22 v P31 ^ ! P11 v B21 ^ ! P22 v B21 ^ ! P31 v B21 , ! B11 , B21 |= ! P12

#3.
# ! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= ! Mythical
# ! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= Mythical
# ! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= ! Magical
# ! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= Magical
# ! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= ! Horned
# ! Mythical v ! Mortal , Mythical v Mortal ^ Mythical v Mammal , Mortal v Horned ^ ! Mammal v Horned , ! Horned v Magical |= Horned

#4.a
# ! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= Amy
# ! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= ! Amy
# ! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= Bob
# ! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= ! Bob
# ! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= Cal
# ! Amy v ! Cal , ! Bob v ! Cal ^ Bob v Cal , ! Cal v Bob v ! Amy ^ Cal v ! Bob ^ Cal v Amy |= ! Cal
        
#4.b
# ! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= Amy
# ! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= ! Amy
# ! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= Bob
# ! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= ! Bob
# ! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= Cal
# ! Amy v ! Cal ^ Amy v Cal , ! Bob v Amy ^ ! Bob v Cal ^ Bob v ! Amy v ! Cal , ! Cal v Bob ^ ! Bob v Cal |= ! Cal