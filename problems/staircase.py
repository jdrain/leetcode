# given a staircase with N steps, how many combinations of steps that take:
#   i) one step at a time
#   ii) two steps at a time
# can you climb the staircase in

# generate all subsets of 1s and 2s that sum to N where 2s are formed
# by combining adjacent 1s
import time

# get all sets
def generate_sets(N):
    # init
    init_sol = ["1" for i in range(0,N)]
    solutions = set(["".join(init_sol)])
    last_round = [init_sol]
    while last_round:
        tmp = []
        for s in last_round:
            for i in range(0, len(s) - 1):
                if s[i] == "1" and s[i+1] == "1":
                    tmp_ls = s[:i] + ["2"] + s[i+2:]
                    tmp_str = "".join(tmp_ls)
                    if tmp_str not in solutions:
                        tmp.append(tmp_ls)
                        solutions.add(tmp_str)
        last_round = tmp[:]
    return solutions

# this patterns out to the fibonacci sequence...
def count_sets(N):
    fib = [1,2]
    if N <= 2:
        return fib[N-1]
    else:
        i = 2
        while i < N:
            fib.append(fib[i-1] + fib[i-2])
            i += 1
        return fib[N-1]

if __name__ == '__main__':
    now = time.time()
    print(len(generate_sets(25)))
    print("set gen time delta: {}".format(time.time() - now))

    now = time.time()
    print(count_sets(25))
    print("dp fib time delta: {}".format(time.time() - now))
