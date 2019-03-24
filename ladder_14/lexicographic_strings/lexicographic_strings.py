# lexicographic_strings.py
# Name: Sadisha Galappatti
# Date: March 17, 2019



# read input function to read stdin and parse
def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input

# a = 97
# z = 122
# A = 65
# Z = 90
# def compare_strings(strings):
#     sum = range(len(strings))
#     for i,j in enumerate(strings):
#         sum[i] = 0
#         for k in j:
#             chr_val = ord(k)
#             if chr_val <= 90:
#                 sum[i] += chr_val + 32
#             else:
#                 sum[i] += chr_val
#
#     if sum[0] < sum[1]:
#         return -1
#     elif sum[0] == sum[1]:
#         return 0
#     else:
#         return 1

def compare_strings(strings):
    isIdenticalString = True
    str_len = len(strings[0])
    sum = [0, 0]

    # Set both strings to lowercase
    for i, j in enumerate(strings):
        strings[i] = j.lower()

    # The length is guarunteed to be the same for both strings
    iterater = 0
    while(iterater < str_len):
        if ord(strings[0][iterater]) < ord(strings[1][iterater]):
            return -1
        elif ord(strings[0][iterater]) > ord(strings[1][iterater]):
            return 1
        iterater += 1

    return 0


def main():
    strings = read_input(2)
    res = compare_strings(strings)


    print(str(res))



if __name__ == "__main__":
    main()
