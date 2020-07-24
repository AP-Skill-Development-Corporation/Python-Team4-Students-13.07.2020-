def iseven(n):
    if n%2==0:
        return "even"
    else:
        return "false"
def isprime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c=c+1
    if c==2:
        return "prime"
    return "notprime"