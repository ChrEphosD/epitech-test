def star():
  u = float(input("Entrez un chiffre entier svp : "))
  while u.is_integer() != True:
    u = float(input("Entrez un chiffre entier svp : "))
  #the number has to be integer
    
  top = int(3*u)#variable that calculate the first * position
  
  if u == 0:
    pass
  elif u ==1:
    print("""   *
*** ***
 *   *
*** ***
   *   """)
#if 0 end without error, if 1 print the star bellow, else start program
  else:
    print((top-1)*" "+"*") #print the top *
    u2 = u
    while u2 > 1:
      space_before = int(top + u2 - u - 2)
      space_after = int((-u2 + u)* 2 + 1)
      print(" "*space_before+"*"+" "*space_after+"*")
      u2 = u2-1
#print the top part of the star
      
    u_between = int(2*u-3)
    print("*"*int(2*u+1)+" "*u_between+"*"*int(2*u+1))
#print the long line of *    

    u3 = u
    while u3 > 0:
      space2_before = int(1+u-u3)
      space2_after = int(2*(2*u+1)+u_between-4-2*(u-u3))
      u3 = u3-1
      print(" "*space2_before+"*"+" "*space2_after+"*")
#print second part of the star

    while u3 < u-1:
      space2_before = space2_before - 1
      space2_after = space2_after + 2
      u3 = u3+1
      print(" "*space2_before+"*"+" "*space2_after+"*")
#print 3rd part which is 2nd  in reverse

    print("*"*int(2*u+1)+" "*u_between+"*"*int(2*u+1))
#print the second long line of *

    u4 = u
    while u4 > 1:
      print(" "*space_before+"*"+" "*space_after+"*")
      space_before = space_before + 1
      space_after = space_after - 2
      u4 = u4-1
#print the bottom part of the star, which is top part in reverse
      
    print((top-1)*" "+"*")
#print the last * at the very bottom
