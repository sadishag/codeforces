# presents.py
# Name: Sadisha Galappatti
# Date: March 13, 2019
# codeforces link: http://codeforces.com/problemset/problem/61/A

# read input function to read stdin and parse
def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input


def main():
    numbers = read_input(2)
    count = len(numbers[0]) - 1
    res = ""
    while count >= 0:
        if numbers[0][count] == numbers[1][count]:
            res += "0"
        else:
            res += "1"
        count -= 1

    print(res[::-1])



if __name__ == "__main__":
    main()
