"""
Given a set of distinct integers, print the size of a maximal subset of S where the sum of any numbers in S
is not evenly divisible by K.
"""


def init():
    # link to the file
    input_link = "input/input16.txt"
    try:
        file = open(input_link, "r")
        file_data = file.readlines()
        file.close()
    except IOError:
        print("file doesn't exist!")
        return

    #subset_stats = input("Enter n and k: ")
    #subset_values = input("Enter numbers: ")

    # converting str to int
    subset_stats = list(map(int, file_data[0].split()))
    subset_values = list(map(int, file_data[1].split()))

    # making sure there's only two values on first line and 1 >= K <= 100
    if len(subset_stats) != 2 and 1 >= subset_stats[1] <= 100:
        print("wrong input on first line")
        return
    # checking length of S
    if len(subset_values) == subset_stats[0] and 1 >= subset_values[0] <= 100000:
        print("wrong input on second line")
        return

    def count_occurrences(current_num):
        occurrences = 0
        for elm in subset_values:
            # skipping first elm
            if current_num != elm:
                permutation = current_num + elm
                #print(str(int(current_num)) + "+" + str(int(elm)) + "=" + str(permutation))
                if permutation % subset_stats[1] == 0:
                    occurrences += 1
                    #print([current_num, occurrences])
        return [current_num, occurrences]

    def check_max_occurrences():
        max_occurrences = [0, 0]
        for elm in subset_values:
            if max_occurrences[1] < count_occurrences(elm)[1]:
                max_occurrences = count_occurrences(elm)
        return max_occurrences

    for val in subset_values:
        if check_max_occurrences() != [0, 0]:
            subset_values.remove(check_max_occurrences()[0])

    # getting input number
    link_num = "".join(filter(str.isdigit, input_link))
    file = open("output/output" + link_num + ".txt", "w")
    file.write(len(subset_values).__str__())

    return


init()
