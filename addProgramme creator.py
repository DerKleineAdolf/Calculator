
with open ("Code Add.txt", "a") as f:  
    f.write ('n1 = int(input("Premier nombre : "))\n')
    f.write ('n2 = int(input("Deuxieme nombre : "))\n')
    f.close ()

for j in range(0,3000):
    for h in range(0,3000):
        with open ("Code Add.txt", "a") as f:  
            f.write ('if n1 == {0} and n2 == {1}:\n'.format(j,h))
            f.write ('  print("{0} x {1} = {2}".format(n1,n2,n1*n2))\n')
            f.close ()
    
    



