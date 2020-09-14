
#!-------------- Unification ---------------!
class A:
 R1,R2,j = 0,0,0
 l10,l20,lst1,lst2 = [],[],[],[]
 def Automate(self,etat,S):
        i,nb1,nb2 = 0,0,0
        stack = True
        for i in range(len(S)):

            if etat == 0:
               if S[i] >= 'a' and S[i] <= 'z':
                  etat = 0
               elif S[i] == '(':
                  etat =1;nb1+=1
               else : stack = False

            elif etat == 1:
               if S[i] >= 'a' and S[i] <= 'z':
                    etat =2
               elif S[i] >= 'A' and S[i] <= 'Z':
                    etat =3
               elif S[i] >= '0' and S[i] <= '9' :
                    etat =4
               else : stack = False

            elif etat == 2 :
               if S[i] >= 'a' and S[i] <= 'z':
                    etat =2
               elif S[i] == ')':
                    etat =6;nb2+=1
               elif S[i] == ',' :
                    etat =5
               elif S[i] == '(':
                    etat =1;nb1+=1
               else :stack = False

            elif etat == 3:
               if S[i] == ')':
                    etat =6;nb2+=1
               elif S[i] == ',':
                    etat =5;
               else :stack = False

            elif etat == 4:
                if S[i] == ')':
                    etat =6;nb2+=1
                elif S[i] >= '0' and S[i] <= '9':
                    etat = 4
                elif S[i] >= ',' :
                    etat = 5
                else: stack = False;
            elif etat == 5:
                if S[i] >= 'a' and S[i] <= 'z':
                    etat = 2
                elif S[i] >= 'A' and S[i] <= 'Z':
                    etat = 3
                elif S[i] >= '0' and S[i] <= '9' :
                    etat = 4
                else :stack = False
            elif etat == 6:
                if S[i] == ',':
                    etat = 1
                elif S[i] == '.':
                    etat = 7

                elif S[i] == ')':
                    etat =6;nb2+=1
                else: stack = False

            elif etat == 7:
                 if S[i] == ' ':
                    etat = 7
                 else:
                    stack = False
            i+=1

        if etat != 7 or nb1 != nb2:
            stack = False

        return stack
 # ///// function get nom of any function
 def getNom(self,f):
     i=0
     s=' '
     while i < f.index('('):
         s=f[:f.index('(')]
         i+=1
     return s

# function special get parameter
 def getParametre(self,f):
    i,bb,n1,n2,l,lst = 0,0,1,1,[],[]
    cc = 0
    for i in range(len(f)):
        if f[i] == "(":
            bb+=1
        elif f[i] == ")":
            cc+=1
        if f[i] == "(" and n1 == 1 :
            j = f.index('(');l.append(j);n1=0
        elif f[i] == ',' and (bb == 1 or cc == bb-1):
            k = i;l.append(k)
        elif f[i] == '.' and n2 == 1:
            q = f.index('.')-1;l.append(q);n2=0
        i+=1

    i = 0
    while len(l) != 1:
        par = f[l.pop(0)+1:l[0]]
        lst.append(par)
    return lst


#//////function check Variable
 def isVar(self,v):

    if v >= 'A' and v <= 'Z' and len(v)==1:
        return True
    else :
        return False

#//////function check Constant or Number
 def isConst(self,c):
    i,const = 0,False
    while i in range(len(c)):
       if (c[i] >= 'a' and c[i] <= 'z') or (c[i] >= '1' and c[i] <= '9'):
          const = True
       else:
          return False
       i+=1
    return const

#//////function check Function or Not
 def isFunc(self,f):
    i = 0
    while i in range(len(f)):
       if f[i] == "(":
          return True
       i+=1
    return False

#/////// function sépare parametre et stocké dans list
 def separé2(self,f):
    ww = f[f.index('(')+1:f.index('.')-1]
    xx = ww.split(',')
    return xx

# !!************** commencer regle 3 **************!!
 def regle3(self,chek1,chek2,f1,f2):
    self.j+=1
    if chek1 == True and chek2 == True :
      if self.getNom(f1) == self.getNom(f2):  # test f1 and f2 are they have same name
        self.lst1 = self.getParametre(f1)     # so same name!,then get parametre for them and put on 2 list
        self.lst2 = self.getParametre(f2)     #------------!,
        if len(self.lst1) == len(self.lst2) : # test f1 and f2 are they same nomber of parameter
          if self.j==1:
            print("*/*/ app R3 :")
            i = 0
            self.l10 = self.lst1.copy()
            self.l20 = self.lst2.copy()
            #print (l1,l2)
            while i < len(self.lst1) :
               print("------> ",self.lst1[i],"=",self.lst2[i])
               i+=1
            print("\n","---------------------------------------")

          else :
               k = 0
               print("*/*/ app R3 :")
               self.l10.extend(self.lst1);#print("##",self.l10,self.lst1)
               self.l20.extend(self.lst2)
               for k in range(len(self.l10)) :
                print("------> ",self.l10[k],"=",self.l20[k])
               k+=1
               print("\n","--------------------------------------")
               #self.lst1 = self.l10.copy()
               #self.lst2 = self.l20.copy()
          self.appR()
        else:
            print("Impossible Unification R3: number of parameter for ",f1," and ",f2," are different")
      else:
          print("Impossible Unification R3: name of function '",self.getNom(f1),"' != '",self.getNom(f2),"'are diffrent")
    else :
        print("Erreur Syntaxic invalid syntax for write '",self.getNom(f1),"' or '",self.getNom(f1),"'")
#!!**************** commencer regle 1 ********************
 def regle1(self):
      i = 0
      print("*/*/ app R1 :")
      while i < len(self.l10):
        if self.isVar(self.l20[i]) == True and self.isVar(self.l10[i])==False :
            print("------>!* ",self.l20[i],"=",self.l10[i])
            p1 =self.l10.pop(i);p2 =self.l20.pop(i)
            self.l10.insert(i,p2);self.l20.insert(i,p1)
        else :
            print("------> ",self.l10[i],"=",self.l20[i])
        i+=1
      print("\n","---------------------------------------")
      self.R1 = 0

#!!**************** commencer regle 2 ********************
 def regle2(self):
    i,TT = 0,[]
    print("*/*/ app R2 :")
    while i in range(len(self.l10)):
        if self.l10[i] == self.l20[i] :
            TT.append(self.l10.pop(i));self.l20.pop(i)
            i-=1
        else:
            print("------> ",self.l10[i],"=",self.l20[i])
        i+=1
    TT = ' | '.join(str(x) for x in TT)
    print("supprimer ",TT,"\n\n","---------------------------------------")
    self.R2 = 0


# function General for applique regles R1 R2 R3

 def appR(self):


    i = 0
    while i in range(len(self.l10)):
        if self.isVar(self.l20[i]) == True and self.isVar(self.l10[i])==False :
            self.R1 = 1
        if self.l10[i] == self.l20[i] :
            self.R2 = 1

        i+=1

    if self.R1 == 1:
       self.regle1() #----- call regle 01
    if self.R2 == 1:
       self.regle2() #----- call regle 02
    i = 0
    #----- call regle 03
    while i in range(len(self.l10)):
        if self.isFunc(self.l10[i]) == self.isFunc(self.l20[i]) == True :
            f1=self.l10.pop(i);f2=self.l20.pop(i)
            f1+='.';f2+='.'
            self.regle3(self.Automate(0,f1),self.Automate(0,f2),f1,f2)
            #-----  regle 03
        i+=1


f1 = "f(x,X,100,g(L,hh),rt(100,n))."
f2 = "f(df(u),X,R,g(500,K),rt(S,V))."
F1 = "fx(v,g(h(x,2,z(9999)),K),M)."
F2 = "fx(B,g(h(Y,n,m(P)),K),1)."

print("write function :\n")
#s = str(input())

#result = Automate(0,f2)

#print("------> ",result," <-------")
print("sesie first function :")
g1= str(input())
print("\n")
print("sesie second function :")
g2= str(input())
print("\n")
bb = A()
bb.regle3(bb.Automate(0,g1),bb.Automate(0,g2),g1,g2)



print("\n\n\n\n")
print("############### in futur i will be create Regle 4 by friends ******************!!")


