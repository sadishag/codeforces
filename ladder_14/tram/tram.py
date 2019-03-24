# tram.py
# Name: Sadisha Galappatti
# Date: March 22, 2019

def read_input(n):
    input = []
    for i in range(n):
        input.append(raw_input())
    return input

def track_line(in_out):
    capacity = 0
    local_max = 0
    for i in in_out:
        direction = i.split(" ")
        go_out = int(direction[0])
        go_in = int(direction[1])
        capacity = capacity - go_out + go_in
        if capacity > local_max:
            local_max = capacity

    return local_max



def main():
    num_lines = read_input(1)
    content = read_input(int(num_lines[0]))

    print(track_line(content))




if __name__ == "__main__":
    main()
