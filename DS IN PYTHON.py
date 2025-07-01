
#data structures
#builtin ds
'''1.list
2.tuple
3.set
4.dict
5.string

.modules
.collection
.deque'''

#DS MODULES
'''1.array/lists #linear ds
2.string #linear ds
3.tacks #linear ds
4.queues #linear ds
5.linked list #linear ds
6.hashing/hashtables #linear ds
7.sets #non linear
8.TREES #non linear
9.graphs  #non linear
10.heaps/priority queue  #non linear (abstact ds)
11.trie-prefix #non linear(abstarct ds)
12.recursion/back tracking
13.searching
14.sorting
15.greedy/brute force'''

#array operations 
'''program to consider a list arr=[10,20,0,40] and perform insert operation 
with 50 and 25 at position 2 respectively,dlt 30 and
traverse the array to fetch a num 25 is present or not'''
arr=[10,20,30,40]
#insert
arr.append(50)
arr.insert(2,25)
#print(arr)
for i in arr:
    print(i,end=' ')
#deletion
arr.remove(30)
arr.pop()
#print(arr)
#traversal
for i in arr:
    print(i,end=' ')
#searching
print("\n 25 in array?",25 in arr)

'''prgrm to check whether the given string is palindrome
or not and count the palandromic character which are repeated  
str=madam
output:{'m':2,'a':2,'d':1}
str=malayalam'''
text=input("enter a name:")
if text==text[::-1]:
    print("palindrome")
else:
    print("not")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)

# SEARCHINGS
'''.linear
.binary
.sential search
.fibonacci search
.interpolation search'''

#LINEAR SEARCH: 
'''in sorted or unsorted arrays
 [45,-9,77,32]'''
#ALGORITHM 
'''1.arr of list of size n
2.key for search element
3.start with zero index
4.compare arr[i]==key
     arr[i]=key return index
     else not(move to next index)
5.repeat same steps till n-1
6.if no match return -1     '''
#CODE
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
size=int(input("enter the size of array:"))
arr=[]
print("enter the element: ")
for i in range (size):
    num=int(input(f"element{i+1}:"))
    arr.append(num)
key=int(input("enter the element to search:"))
result=linear_search(arr,key)
if result!=-1:
    print(f"\n element{key} found at {result}")
else:
    print(f"\n element {key} not found at {result}")   

#BINARY SEARCH ALGORITHM
'''1.array must be soted
2.array is divided in to 2 seperate equivalent halfs
        set low & high 0 -> n-1
        condition low <= high
        mid= low+high//2 
        arr[mid]==key return mid
        arr[mid]<key low mid+1
        arr[mid]key high mid-1
        not found return -1'''
#CODE
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1  
    return -1          
size=int(input("enter the size of array:"))
arr=[]
print("enter the element: ")
for i in range (size):
    num=int(input(f"element {i+1}:"))
    arr.append(num)
key=int(input("enter the element to search:"))
result=binary_search(arr,key)
if result!=-1:
    print(f"\n element{key} found at {result}")
else:
    print(f"\n element {key} not found at {result}")   

