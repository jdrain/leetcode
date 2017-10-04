# tests to compare quicksort and optimized quicksort
import random, time, sys
import matplotlib.pyplot as plt
from formatError import ArgFormatError
from fundamentals import quicksort, quicksort_op

# generate the test cases
def gen_tests(elem_range, test_size, list_size):
    return [[random.randint(0,elem_range) for i in range(0,test_size)] for i in range(0,list_size)]

# parse the command line arguments
def parse_args(args):
    print(args)
    arg_dict = {}

    arg_len = len(args)
    i = 1
    while i < arg_len:
        if args[i] == "--range":
            i += 1
            arg_dict["range"] = int(args[i])
            if not arg_dict["range"]: return {}
            i += 1

        elif args[i] == "--t_size":
            i += 1
            arg_dict["test size"] = int(args[i])
            if not arg_dict["test size"]: return {}
            i += 1

        elif args[i] == "--arr_size":
            i += 1
            arg_dict["list size"] = int(args[i])
            if not arg_dict["list size"]: return {}
            i += 1

        elif args[i] == "--graph":
            arg_dict["graph"] = True
            i += 1



    return arg_dict

# main function to run the test cases
if __name__ == '__main__':

    args = parse_args(sys.argv)

    # default params if none are entered
    if "range" not in args.keys():
        args["range"] = 10
    if "test size" not in args.keys():
        args["test size"] = 1000
    if "list size" not in args.keys():
        args["list size"] = 10
    if "graph" not in args.keys():
        args["graph"] = False
    graph = args["graph"]

    # create some large lists to test on
    test_lists = gen_tests(args["range"], args["test size"], args["list size"])

    # display test results
    s = "-----------"
    if graph:
        ratios = []

    for i in range(0,args["list size"]):
        ls1 = test_lists[i][:]
        len_ls1 = len(ls1)
        ls2 = test_lists[i][:]
        len_ls2 = len(ls2)

        print("{} list #{} {}".format(s,i+1,s))

        # benchmark regular quicksort
        ti1 = time.time()
        quicksort.quicksort(ls1, 0, len_ls1 - 1)
        reg_t_total = time.time() - ti1
        print("\n{} quicksort {}\n + seconds: {}\n + list size: {}\n".format(s,s,reg_t_total,len_ls1))

        # benchmark optimized quicksort
        ti2 = time.time()
        quicksort_op.quicksort(ls2, 0, len(ls2) - 1)
        op_t_total = time.time() - ti2
        print("{} optimized {}\n + seconds: {}\n + list size: {}\n".format(s,s,op_t_total,len_ls2))

        # collect data for graph
        if graph:
            ratios.append(reg_t_total/op_t_total)

    print("{}{}{}".format(s,s,s))

    # graph data
    if graph:
        plt.plot([i for i in range(1, args["list size"] + 1)] , ratios, "ro")
        plt.ylabel("op time/reg time")
        plt.title("ratio of optimized quicksort to regular implementation")
        plt.show()
