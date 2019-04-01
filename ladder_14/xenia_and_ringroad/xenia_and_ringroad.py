# amusing_joke.py
# Name: Sadisha Galappatti
# Date: March 24, 2019
# codeforces link: http://codeforces.com/problemset/problem/136/A

import pdb
# read input function to read stdin and parse
def read_input(n):
    in_args = []
    for i in range(n):
        in_args.append(input())
    return in_args

def task_timer(n, m, a):
    count = 0
    for i in range(1, m):
        if a[i-1] > a[i]:
            count += 1

    res = count * n + a[-1] - 1
    return res

def main():
    inputs = read_input(2)
    n_m = inputs[0].split(" ")
    n = int(n_m[0])
    m = int(n_m[1])
    a = [int(i) for i in inputs[1].split(" ")]

    print(str(task_timer(n, m, a)))



if __name__ == "__main__":
    main()
