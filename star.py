def star():
  suit = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
  #suite qui va servir pour la branche du haut.

  u = float(input("Entrez un chiffre entier svp"))
  while u.is_integer() != True:
    u = float(input("Entrez un chiffre entier svp"))
  #le chiffre qu'on rentre doit etre entier
    
  top = int(3*u)#variable qui calcule la pos de l'asterisque tout en haut
  
  if u == 0:
    pass
  elif u ==1:
    print("""   *
*** ***
 *   *
*** ***
   *   """)
#si 0 fin sans erreur, si 1 print l'etoile cidessus et sinon lancer le programme cidessous
  else:
    print((top-1)*" "+"*") #print l'astérisque du haut
    u2 = u
    while u2 > 1:
      space_before = int(top+u2-u-2)
      space_after = int(suit[int(-u2+u)])
      print(" "*space_before+"*"+" "*space_after+"*")
      u2 = u2-1
#cette partie permet de print tout la partie du haut
      
    u_between = int(2*u-3)
    print("*"*int(2*u+1)+" "*u_between+"*"*int(2*u+1))
#cette partie print la longue ligne d'*    

    u3 = u
    while u3 > 0:
      space2_before = int(1+u-u3)
      space2_after = int(2*(2*u+1)+u_between-4-2*(u-u3))
      u3 = u3-1
      print(" "*space2_before+"*"+" "*space2_after+"*")
#cette partie print la deuxieme partie de l'etoile

    while u3 < u-1:
      space2_before = space2_before - 1
      space2_after = space2_after + 2
      u3 = u3+1
      print(" "*space2_before+"*"+" "*space2_after+"*")
#cette 3e partie reprend la deuxieme à l'envers

    print("*"*int(2*u+1)+" "*u_between+"*"*int(2*u+1))
#print la deuxieme longue ligne d'asterisques

    u4 = u
    while u4 > 1:
      print(" "*space_before+"*"+" "*space_after+"*")
      space_before = space_before + 1
      space_after = space_after - 2
      u4 = u4-1
#cette partie print la branche du bas (partie du haut à l'envers)
      
    print((top-1)*" "+"*")
#print l'astrisque tout en bas
