import sys

#take in the desired index of fibonacci number as a command
#line arg

if len(sys.argv)!=2:
    print("Please enter the desired index of fibonacci number"
    " as a command line argument")

n1 = int(sys.argv[1])

def recursiveFib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recursiveFib(n-1) + recursiveFib(n-2)

print("Fibonacci(%d) is : %d" % (n1, recursiveFib(n1)))
