# way_too_long_words.py
# Name: Sadisha Galappatti
# Date: March 25, 2019
# codeforces link: http://codeforces.com/problemset/problem/71/A

# read input function to read stdin and parse
# returns an array
def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input


def main():
    n = read_input(1)
    words = read_input(int(n[0]))
    for i in words:
        i_len = len(i)
        if i_len > 10:
            print(i[0] + str(i_len - 2) + i[i_len - 1])
        else:
            print(i)
    return



if __name__ == "__main__":
    main()
