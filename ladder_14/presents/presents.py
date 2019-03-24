# presents.py
# Name: Sadisha Galappatti
# Date: March 13, 2019


# read input function to read stdin and parse
def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input

# Function to convert single digit or array of digits to ints
def str_to_int(str_val):
    # Need to assign res to be an array to append to it
    res = []
    try:
        for i, j in enumerate(str_val):
            res.append(int(j))
    except:
        print("please provide valid ints")
        res = str_val
    return res


# Function to actually run the algorithm
def inverse_presents(n, arr):
    tmp = 0
    result = range(n)
    for i, j in enumerate(arr):
        tmp = j - 1
        result[tmp] = i + 1
    return result

def print_output(arr):
    res_str = ""
    for i in arr:
        res_str = res_str + str(i) + " "
    return res_str


# Main function calls read input
def main():
    num_lines = 2
    in_arr = read_input(num_lines)
    num_friends = int(in_arr[0])
    if len(in_arr[1]) == 1:
        gift_direction = [int(in_arr[1])]
    else:
        gift_direction = str_to_int(in_arr[1].split(" "))

    inverse_res = inverse_presents(num_friends, gift_direction)
    print(print_output(inverse_res))

    # print("Number of friends: " + str(type(num_friends)))
    # print("Gift direction: " + str(gift_direction))

if __name__ == "__main__":
    main()
