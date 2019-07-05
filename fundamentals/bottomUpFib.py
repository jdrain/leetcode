import sys

#take in the fibonacci number as an argument
if len(sys.argv) != 2:
    print("please enter the index of the desired fibonacci"
    " number as an argument")
#bottom up fibonacci implementation
def bottomUpFib(n):
    init_ls = [0 for i in range(0,n)]
    init_ls[0:1] = [1,1] #base case for first two fibonacci numbers
    
    #calculate the fibonacci numbers from the bottom up
    for i in range(2,n):
        init_ls[i] = init_ls[i-1]+init_ls[i-2]
    return init_ls[n-1]

#implement the program
fib_num = int(sys.argv[1])
print("Fibonacci(%d) is: %d" % (fib_num,bottomUpFib(fib_num)))
