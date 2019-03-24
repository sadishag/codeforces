# nearly_lucky_number.py
# Name: Sadisha Galappatti
# Date: March 17, 2019
# codeforces link: http://codeforces.com/problemset/problem/110/A


# read input function to read stdin and parse
def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input


# Main function calls read input
def main():
    number = read_input(1)
    # print(number[0])
    count = 0
    for i in number[0]:
        if i == "4" or i == "7":
            count += 1

    if count == 4 or count == 7:
        print "YES"
    else:
        print "NO"

if __name__ == "__main__":
    main()
