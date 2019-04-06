# casia_and_pylons.py
# Name: Sadisha Galappatti
# Date: April 1, 2019
# codeforces link: http://codeforces.com/problemset/problem/463/B

# read input function to read stdin and parse
def read_input(n):
    in_args = []
    for i in range(n):
        in_args.append(input())
    return in_args

def calculate_min_cost(n, h):
    if n == 1:
        return h[0]

    cost = h[0]
    energy = 0
    for i in range(n - 1):
        e_needed = h[i] - h[i + 1]
        energy += e_needed
        if  energy < 0:
            cost += abs(energy)
            energy += abs(energy)

    e_needed = h[-2] + h[-1]
    energy += e_needed
    if energy < 0:
        cost += abs(energy)
        energy += abs(energy)

    return cost


def main():
    inputs = read_input(2)
    n = int(inputs[0])
    h = [int(vals) for vals in inputs[1].split(" ")]

    print(str(calculate_min_cost(n, h)))



if __name__ == "__main__":
    main()
