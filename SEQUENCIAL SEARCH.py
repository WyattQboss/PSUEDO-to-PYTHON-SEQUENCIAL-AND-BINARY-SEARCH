#SELECTION SORT

arr = (1,2,87,65,98,345,356,23,986)
Found = False #CAN ALSO JUST PUT BREAK AT THE BOTTOM TO BREAK OUT OF THE LOOP
number = int(input("GIVE ME A NUMBER"))

for i in range (0, len(arr)):
    if number == arr[i] and Found == False:
        print ("you found the number", number, "at index", i)
        Found = True





