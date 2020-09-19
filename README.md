[unify1](screenshot/unify1.png)
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
## Unification of two predicates:
Let ***P1(t1, t2, ......,tn)*** and ***P2(t1’, t2’, .........,tm’)***
If ***(P1 ≠ P2)*** or ***(P1 = P2 and n ≠ m)*** then the unification is impossible
otherwise if **P1 = P2** and **n = m** then unification will be possible if we
can unify the terms **ti** and **ti’** 2 to 2.
