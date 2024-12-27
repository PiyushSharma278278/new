strings="hello bhai"
# a=strings.split()
# new=[]
# string=""
# for words in a:
#     rev=words[::-1]
#     new.append(rev)
# string=' '.join(new)
# print(string)
# arr=[]
# for i in range(0,10,1):
#     n=int(input())
#     arr.append(n)
# print(arr)
# a=sum(arr)
# print(a)
# new=strings.split()
# new1="".join(new)
# print(new1)
# print(new1.isalpha())
# print(strings.isalpha())
# print(len(strings))
arr = [7,2,3,4,5]
# size = int(input())
# for i in range(0,size):
#   arr.append(int(input()))
# index1 = int(input())
# index2 = int(input())

# def swap(index1,index2,arr,size):
#     if index1 < 0 or index2 < 0 or index1 >= size or index2 >= size:
#         print("Enter the valid positions to be swapped")
#     else:
#         arr[index1], arr[index2] = arr[index2], arr[index1]
#         print(arr)
        
# swap(index1,index2,arr,size)
# arr.sort(reverse=True)  
# print(arr)
# new=strin.split()
# strin="Hello Bhai"
# l=[]
# for i in strin:
#     if i.islower():
#         l.append(i.upper())
#     else:
#         l.append(i.lower())
# l1="".join(l)
# print(l1)
# l=[1,24,3,5,2,2]
# l.sort(reverse=True)

# print(l)
# l2=set(l)
# print(l2)
# l=list(l2)
# print(l)
# print(l[3:])
# ab=int(input())
# is_prime = True  # Assume the number is prime
# for a in range(2,ab):
#     if ab%a==0:
#         is_prime=False
#         break

# if is_prime:
#     print("Prime")
# else:
#     print("not prime")
# better approach
# ab = int(input("Enter a number: "))

# if ab < 2:
#     print("Not prime")  # Numbers less than 2 are not prime
# else:
#     is_prime = True  # Assume the number is prime
#     for a in range(2, ab):
#         if ab % a == 0:
#             is_prime = False  # Set flag to False if a divisor is found
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not prime")

# string="kaljj"
# for i in range(len(string)):
#     a=string[i:]
#     print(a)
# n=6
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("#",end=" ")
#     print()
    

# string="215363 "
# def leng(string):
#     store=max(string)
#     storemin=min(string)
#     return (store,storemin)
# a,b=leng(string)
# print(a)
# print(b)
# n=6
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
vcount = 0
ccount = 0
dcount = 0
vowel = "aeiouAEIOU"

def countCharacters(string):
    global vcount, ccount, dcount  # Declare global variables
    for char in string:  # Iterate over each character in the string
        if char.isalpha():
            if char in vowel:  # Check if the character is a vowel
                vcount += 1
            else:  # Otherwise, it's a consonant
                ccount += 1
        elif char.isdigit():
            dcount += 1
        else:
            print(f"Invalid character: {char}")

# Example usage
countCharacters("wadkjbawkdb1")
print("Vowel count:", vcount)
print("Consonant count:", ccount)
print("Digit count:", dcount)
