# football.py
# Name: Sadisha Galappatti
# Date: April 1, 2019
# codeforces link: http://codeforces.com/problemset/problem/96/A

# read input function to read stdin and parse
def read_input(n):
    in_args = []
    for i in range(n):
        in_args.append(input())
    return in_args


def is_dangerous(positions):
    max = 1
    counter = 1
    for i in range(1, len(positions)):
        if positions[i - 1] == positions[i]:
            counter += 1
        else:
            counter = 1

        if counter >= max:
            max = counter

    if max >= 7:
        return True
    else:
        return False

def main():
    inputs = read_input(1)[0]

    if is_dangerous(inputs):
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    main()
