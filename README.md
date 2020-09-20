![unify1](screenshot/unify1.png)                                          
#### Overview
this programm it made to learn the important uses of data structur on developement cycle when you go to make your application
we focus on list `[]` how manuplate and you will see the profit of using lists in programming and how much we need them during
build an application.

# Susbstitution and Uniffication

the unification of two terms **T** and **T'** with variables ***x1, x2, .... xn*** consists in finding a substitution of these
variables by terms ***u1, u2, .... un*** one such as the application
of this substitution makes the terms **T** and **T'** equal.
- applying a substitution ***O = {x1/u1, x2/u2, .... xn/un}*** at a term **T**, produces a new term **T'** obtained by
  replacing each occurrence of **xi** by **ui** in **T**.
- Two formulas are unified, if there is a substitution **O** such that **TO** = **T’O**. 
 and **O** it call to unify **T** and **T’**
>### important note
> *what signify '**term**': term= function/{f(a,..,g(z)),...,heq(55,V)} **or** variable:{A,B,C,...,Z} **or** constant:{Numbers{1,2,...,n}/ words{ab,abc,...,e,d,...,bc..n}}*
## Unification of two predicates:
Let ***P1(t1, t2, ......,tn)*** and ***P2(t1’, t2’, .........,tm’)***
If ***(P1 ≠ P2)*** or ***(P1 = P2 and n ≠ m)*** then the unification is impossible
otherwise if **P1 = P2** and **n = m** then unification will be possible if we
can unify the terms **ti** and **ti’** 2 to 2.
## Unification Algorithme
in this section we're going to express and show **rules** exactly 4 rules which those rules represent the principal part of our program the unification algorithm.
- **rule 1:** Convert **t = x** to **x = t** if **x** is a variable and **t** is not a variable.
- **rule 2:** delete operations of the form **x = x**.
- **rule 3:** Let say **t’= t’’** which **t’** and **t’’** are not variables, if the functions of **t'** and **t''** are not the same then unification is impossible. 

         ``` otherwise replace the equation f(x1’, x2’,..., xn’) = f(x1’’, x2’’,..., xn’')
         
                                          with the equations x1’ = x1’’
                                                             x2’ = x2’’
                                                             ........
                                                             xn’ = xn’’```
                               
