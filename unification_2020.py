
import time as t

#!-------------- Unification ---------------!
class unif:
 R1,R2,j = 0,0,0
 l10,l20,lst1,lst2 = [],[],[],[]
 def Automate(self,etat,S):
        S+='.'
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
 #...Function get name of any input function: f(x,y)----> name = f
 def getName(self,f):
     i=0
     s=' '
     while i < f.index('('):
         s=f[:f.index('(')]
         i+=1
     return s

 #...Function get parameter of any input f function: f(x,y,g(k))----> variables = ['x','y','g(k)']
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


#...isVar check input v it is Variable or not: v=D---> True; v=55/f(S)---> not
 #Note: variable means alphabetical charactere and be capital v={A,B,...,Z}
 def isVar(self,v):

    if v >= 'A' and v <= 'Z' and len(v)==1:
        return True
    else :
        return False

#...isVar check input c it is Constant or not: c={string:ahmed,b,aas,blabla...bla}/{1,2,...,n}---> True; else ---> not
 def isConst(self,c):
    i,const = 0,False
    while i in range(len(c)):
       if (c[i] >= 'a' and c[i] <= 'z') or (c[i] >= '1' and c[i] <= '9'):
          const = True
       else:
          return False
       i+=1
    return const

#...isFunc check input f it is function or not: f=g(x)---> True; f=T---> False
 def isFunc(self,f):
    i = 0
    while i in range(len(f)):
       if f[i] == "(":
          return True
       i+=1
    return False

# !!************** start rule 3 **************!!
 def rule3(self,chek1,chek2,f1,f2):
    self.j+=1
    if chek1 == True and chek2 == True :
      if self.getName(f1) == self.getName(f2):  # test f1 and f2 are they have same name
        self.lst1 = self.getParametre(f1)     # so same name!,then get parametre for them and put on 2 list
        self.lst2 = self.getParametre(f2)     #------------!,
        if len(self.lst1) == len(self.lst2) : # test f1 and f2 are they same nomber of parameter
          if self.j==1:
            print("\033[1;36;40m*/*/*/ apply R3 :\033[0m")
            print ("\033[1;32;48m[*] extract parameter from:",f1,"=",f2,"\033[0m")
            i = 0
            self.l10 = self.lst1.copy()
            self.l20 = self.lst2.copy()
            #print (l1,l2)
            while i < len(self.lst1) :
               t.sleep(0.3)
               print("------> ",self.lst1[i],"=",self.lst2[i])
               i+=1
            print("\n\033[1;33;40m---------------------------------------\033[0m")

          else :
               k = 0
               print("\033[1;36;40m*/*/*/ apply R3 :\033[0m")
               print ("\033[1;32;48m[*] extract parameter from:",f1,"=",f2,"\033[0m")
               self.l10.extend(self.lst1)
               self.l20.extend(self.lst2)
               for k in range(len(self.l10)) :
                   t.sleep(0.3)
                   print("------> ",self.l10[k],"=",self.l20[k])
               k+=1
               print("\n\033[1;33;40m--------------------------------------\033[0m")
          self.allRules()
        else:
            print("\033[1;31;47m[!] Impossible Unification R3: number of parameter are different for \033[0m",f1," and ",f2,)
      else:
          print("\033[1;31;47m[!] Impossible Unification R3: Functions names mismatch \033[0m'",self.getName(f1),"' != '",self.getName(f2))
    else :
        print("\033[1;31;47m[!] Erreur Syntaxic invalid syntax for write \033[0m'",f1,"' or '",f2,"'")
#!!**************** start rule 1 ********************
 def rule1(self):
      i = 0
      print("\033[1;36;40m*/*/*/ apply R1 :\033[0m")
      while i < len(self.l10):
        t.sleep(0.3)
        if self.isVar(self.l20[i]) == True and self.isVar(self.l10[i])==False :
            print("------>\033[1;32;48m[*]",self.l20[i],"=",self.l10[i],"\033[0m")
            p1 =self.l10.pop(i);p2 =self.l20.pop(i)
            self.l10.insert(i,p2);self.l20.insert(i,p1)
        else :
            print("------> ",self.l10[i],"=",self.l20[i])
        i+=1
      print("\n\033[1;33;40m---------------------------------------\033[0m")
      self.R1 = 0

#!!**************** start rule 2 ********************
 def rule2(self):
    i,TT = 0,[]
    print("\033[1;36;40m*/*/*/ apply R2 :\033[0m")
    while i in range(len(self.l10)):
        t.sleep(0.3)
        if self.l10[i] == self.l20[i] :
            TT.append(self.l10.pop(i));self.l20.pop(i)
            i-=1
        else:
            print("------> ",self.l10[i],"=",self.l20[i])
        i+=1
    TT = ' | '.join(str(x) for x in TT)
    print("elements removed ",TT)
    for x in TT:
        print("\033[1;32;48m------> [*] Remove",x,"=",x,)
        print("\n\033[1;33;40m---------------------------------------\033[0m")
    self.R2 = 0


# function General for applique rules R1 R2 R3

 def allRules(self):

    i = 0
    while i in range(len(self.l10)):
        if self.isVar(self.l20[i]) == True and self.isVar(self.l10[i])==False :
            self.R1 = 1
        if self.l10[i] == self.l20[i] :
            self.R2 = 1
        i+=1
    if self.R1 == 1:
       t.sleep(1)
       self.rule1() #----- call rule 01
    if self.R2 == 1:
       t.sleep(1)
       self.rule2() #----- call rule 02
    i = 0
    #----- call rule 03
    while i in range(len(self.l10)):
        if self.isFunc(self.l10[i]) == self.isFunc(self.l20[i]) == True :
            f1=self.l10.pop(i);f2=self.l20.pop(i)
            t.sleep(1)
            self.rule3(self.Automate(0,f1),self.Automate(0,f2),f1,f2)
            #-----  rule 03
        i+=1








