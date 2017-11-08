# find the longest monotonically increasing subsequence
import sys, random

# dynamic programming approach
def get_longest_seq(ls):
    if len(ls)!= 0:
        subseq_ls = [ [ls[0]] ]
        for i in range(1, len(ls)):
            ind = place_num_in_seq(ls[i], subseq_ls, 0, len(subseq_ls) - 1)
            if ind < 0:
                subseq_ls[0][0] = ls[i]
            elif ind == len(subseq_ls) - 1:
                subseq_ls.append(subseq_ls[ind][:] + [ ls[i] ])
            else:
                subseq_ls[ind + 1] = subseq_ls[ind][:] + [ ls[i] ]
        return subseq_ls[len(subseq_ls) - 1]

    else: # if null input return empty list
        return []

# determine how to update the array holding the subsequences
def place_num_in_seq(x, subseq_ls, lo, hi):

    # binary search
    while lo < hi - 1:
        mid = (lo + hi) / 2
        if (x <= subseq_ls[mid][mid]):
            hi = mid
        else:
            lo = mid

    if x <= subseq_ls[lo][lo]:
        return lo - 1
    elif x <= subseq_ls[hi][hi]:
        return lo
    else:
        return hi

if __name__ == '__main__':
    # run a random test case
    test = [random.randint(0,50) for i in range(0,15)]
    print("Initial set: {}\nLongest monotonically increasing subsequence: {}\n".format(test, get_longest_seq(test)))
