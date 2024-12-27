def binaryToDecimal(binary):
    sum=0
    for i in range(0,len(binary)):
        sum+=int(binary[i])*(2**i)
    return sum
n=input()
c=n[::-1]
print(binaryToDecimal(c))
        