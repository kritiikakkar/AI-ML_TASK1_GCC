# Asks the user to enter the number of lists to interleave
n = int(input("Enter a the no. of lists: "))

# Asks the user to enter the length of the list
m=int(input("Enter the length of the list: "))

# Initialize a nested list to create 'n' empty lists to store values
L = [[] for _ in range(n)]

# Taking list values as input from the user 
for i in range (0,n):
      for j in range (0,m):
          a=int(input("%s Element: " %str(j+1)))
          L[i].append(a)
print("The entered lists are: ",L)

# generating interleaved list
final=[]
for i in range (0,n):
      for j in range(0,m):
           final.append(L[j][i])
        
# printing interleaved list 
print ("The interleaved list is: ", final)
