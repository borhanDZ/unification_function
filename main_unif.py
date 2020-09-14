from unification_2020 import unif
print("""\033[1;33;40m
          ______________________( \033[1;35;40mlearn code\33[1;33;40m )_______________________
         |                  _  __ _           _   _                  |
         |      _   _ _ __ (_)/ _(_) ___ __ _| |_(_) ___  _ __       |  
         |+-+-+| | | | '_ \| | |_| |/ __/ _` | __| |/ _ \| '_ \ +-+-+|  
         |+-+-+| |_| | | | | |  _| | (_| (_| | |_| | (_) | | | |+-+-+|   
         |+-+-+ \__,_|_| |_|_|_| |_|\___\__,_|\__|_|\___/|_| |_|+-+-+|   
         |______________________[ unification ]______________________|      
                                                                        
\n
\033[1;37;40m   Hello world, This application called unification is a special
   equation(math equations) have rules to applied it exactly 4 rules
   every rules have caractiristique to achieve.
   we made this app for learn and mastering data structur programing
   and we focus on list[](manipulating and diffirent list method...)\n\n
         \033[1;37;40m[+]---------\033[1;34;40mcoded by: \033[1;36;40m@borhan       \033[1;37;40m----------------------[+]
         [+]---------\033[1;34;40memail:    \033[1;36;40mborhan14041995@yahoo.com\033[1;37;40m -----------[+]
         [+]---------\033[1;34;40mrepo:     \033[1;36;49mhttps://www.github.com/borhanDZ \033[1;37;40m----[+] \033[40m \n
                           \033[1;32;40m+-+-+-+-+-+-+-+-+-+-+-+
                           |u|n|i|f|i|c|a|t|i|o|n|
                           +-+-+-+-+-+-+-+-+-+-+-+
                          
\033[0;33;40mf1 = f(x,X,100,g(L,hh),rt(100,n))
f2 = f(df(u),X,R,g(500,K),rt(S,V))
f3 = fx(v,g(h(x,2,z(9999)),K),M)
f4 = fx(B,g(h(Y,n,m(P)),K),1) \n """)

f1 = "f(x,X,100,g(L,hh),rt(100,n))"
f2 = "f(df(u),X,R,g(500,K),rt(S,V))"
f3 = "fx(v,g(h(x,2,z(9999)),K),M)"
f4 = "fx(B,g(h(Y,n,m(P)),K),1)"
def sesie_func(g1,g2):
    if g1 == 'f1':
        g1 = f1
    elif g1 == 'f2':
        g1 = f2
    elif g1 == 'f3':
        g1 = f3
    elif g1 == 'f4':
        g1 = f4
    if g2 == 'f1':
        g2=f1
    elif g2 == 'f2':
        g2=f2
    elif g2 == 'f3':
        g2=f3
    elif g2 == 'f4':
        g2=f4
    return g1,g2

def main():
  while True:
    print("\033[1;37;40myou can chose to enter one of \033[0;32;40mf1/f2/f3/f4...\033[0m\033[1;37;40mor enter your own function\n")
    print("\033[1;37;40mif you want to exit The programme press \033[0;32;40m'q'\033[37;40m or \033[0;32;40m'Q'\n")
    print("\033[1;36;40m[\033[1;31;40m*\033[1;36;40m]Sesie first function :")
    g1= str(input())
    print("\n")
    print("\033[1;36;40m[\033[1;31;40m*\033[1;36;40m]Sesie second function :")
    g2= str(input())
    print(sesie_func(g1,g2))
    g1,g2 = sesie_func(g1,g2)
    if (g1 or g2) == ('q' or 'Q'):
        break
    app = unif()
    app.rule3(app.Automate(0,g1),app.Automate(0,g2),g1,g2)
    print("\n\n\n\n")
    print("############### in futur i will be create Rule 4 by friends ******************!!")


if __name__ == '__main__':

  try:
      main()
  except KeyboardInterrupt:
      pass
