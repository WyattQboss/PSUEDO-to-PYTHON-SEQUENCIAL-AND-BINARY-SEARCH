#BINARY SEARCH
arr = [1,3,5,7,8,9,12,23,34,56,67,78,95,100,110,120,123,125,127,300,310,325,345,367]
number = 100

minimum = 0
#maximum = len(arr)
#half = int(len(arr)/2)
'''
for i in range (half, maximum):
    if number > arr[half]:
        print ("larger")
        break
    elif number < arr[i]:
        print("smaller")
        break
#print("the full length of the array is " + str(len(arr)) + " values")
#print (int(len(arr)/2))

#print (arr[0:half])
#print (arr[half:maximum])
print(arr)
arr = (arr[half:maximum])
print(arr)
'''


def midpoint():
    global arr
    while len(arr) > 1:
        print (arr)
        maximum = len(arr)
        half = int(len(arr) / 2)
        if number >= arr[half]:
            print("larger")
            arr = arr[half:maximum]
            print (arr)

        elif number <= arr[maximum-1]:
            print("smaller")
            arr = arr[minimum:half]
            print(arr)


midpoint()
