# amusing_joke.py
# Name: Sadisha Galappatti
# Date: March 24, 2019
# codeforces link: http://codeforces.com/problemset/problem/136/A

# read input function to read stdin and parse
def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input

def populate_dict(guest_name, host_name):
    guest_host_name = guest_name + host_name
    char_dict = {}

    for i in guest_host_name:
        if i in char_dict:
            char_dict[i] = char_dict[i] + 1
        else:
            char_dict[i] = 1

    return char_dict

def check_pile_in_char_dict(pile, char_dict):

    for j in pile:
        if char_dict.get(j) == None:
            return False

        if char_dict[j] > 0:
            char_dict[j] -= 1
        else:
            return False
    return True


def main():
    inputs = read_input(3)
    if len(inputs[0]) + len(inputs[1]) != len(inputs[2]):
        print("NO")
        return

    chars = populate_dict(inputs[0], inputs[1])

    if check_pile_in_char_dict(inputs[2], chars):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
