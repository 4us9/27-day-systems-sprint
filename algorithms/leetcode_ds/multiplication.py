#The best case for multiply two n-digit integers is NOT n^2 time.

### Karatsuba Algorithm -- Only One Karatsuba Split ###

#Number 1: 3141592653589793238462643383279502884197169399375105820974944592
#Number 2: 2718281828459045235360287471352662497757247093699959574966967627
def multiply(x, y):
    
    #Need to find base. 
    #base system is 10 and need m that is how many when in half
    #For this q, digit is 64 so half is 32
    m=32
    B=10**m  
    
    #Since a and b are strings, just get the first 32 and last 32
    
    #Step 1 & 2:
    
    #1st digit
    a_str = x[:m]
    b_str = x[m:]

    a = int(a_str)
    b = int(b_str)
    
    #2nd digit
    c_str = y[:m]
    d_str = y[m:]
    
    c = int(c_str)
    d = int(d_str)
    
    #Step 3: (a+b)(c+d) - ac - bd
    step_3 = (a+b)*(c+d) - (a*c) -(b*d)
    
    #Step 4: (ac)(10^2) + (Step 3)(10) + bd
    final = (a*c)*(B**2) + step_3*(B) + b*d
    
    print(final)

    
if __name__ == "__main__":
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    
    multiply(x, y)
    

'''
Example: 83 x 46

Step 1: 
- 8x10 + 3
- 4x10 + 6

Step 2: Find a, b, c, d

a = 8
b = 3
c = 4
d = 6

Step 3: (a+b)(c+d) - ac - bd

(8+3)(4+6) - 32 - 18
= 60

Step 4: (ac)(10^2) + (Step 3)(10) + bd

'''
