#The best case for multiply two n-digit integers is NOT n^2 time.

### Karatsuba Algorithm ###

#Number 1: 3141592653589793238462643383279502884197169399375105820974944592
#Number 2: 2718281828459045235360287471352662497757247093699959574966967627
def multiply(a, b):
    
    #Need to find base. 
    #base system is 10 and need m that is how many when in half
    #For this q, digit is 64 so half is 32
    m=32
    B=10**m  
    
    #Since a and b are strings, just get the first 32 and last 32
    print(a[:m])
    print(b[m:])
    
    
    
    #result1 += helper_multiply(a)
    #result2 += helper_multiply(b)
    
    
    #rint(result1 +result2)

#def helper_multiply(a, b):
#    if: 
#        return
#    else:
        
#        return 
    
if __name__ == "__main__":
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    
    multiply(a, b)
    

'''
Example: 83 x 46

Step 1: 
- 8x10 + 3
- 4x10 + 6

Step 2: Find a, b, c, d

a = 8
b = 3
c = 5
d = 6

Step 3: (a+b)(c+d) - ac - bd

(8+3)(5+6) - 40 - 18
= 63

Step 4: (ac)(10^2) + (Step 3)(10) + bd

'''
