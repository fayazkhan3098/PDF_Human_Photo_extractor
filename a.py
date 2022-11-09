# practical No 2 : to find duplicates from list
# Faiyaz khan section A 74(DSY)
# creating empty list
named1 = []
  
# asking number of elements to put in list
n = int(input("Enter number of elements should be in list: "))
print ('now enter the integer elements one by one')
  
# iterating till num to append elements in list
for i in range(1, n + 1):
    element = int(input("Enter elements: "))
    named1.append(element)
nm=int(input("press any number to find maximum of the given list : "))     
# print maximum element
print("Largest element is:", max(named1))


