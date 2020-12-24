"""
Given a set of distinct integers, print the size of a maximal subset of S where the sum of any numbers in S
is not evenly divisible by K.
"""


def init():
    # link to the file
    input_link = "input/input00.txt"
    try:
        file = open(input_link, "r")
        file_data = file.readlines()
        file.close()
    except IOError:
        print("file doesn't exist!")
        return

    # subset_stats = input("Enter n and k: ")
    # subset_values = input("Enter numbers: ")

    # converting str to int
    subset_stats = list(map(int, file_data[0].split()))
    subset_values = list(map(int, file_data[1].split()))
    n, k = subset_stats

    # making sure there's only two values on first line
    if len(subset_stats) != 2:
        print("wrong input on first line")
        return
    # checking K
    if 1 >= k <= 100:
        print("K is out of scope")
        return
    # checking length of S
    if len(subset_values) != n and len(subset_values) <= 10 ^ 5:
        print("wrong input on second line")
        return
    # checking values in S
    for elm in subset_values:
        if elm < 1 or elm > 100000:
            print("element " + str(elm) + " is out of scope")
            return

    """
    for elm in subset_values:
        data = check_max_occurrences(subset_values, subset_stats)
        if data != [0, 0]:
            subset_values.remove(data[0])
    """
    """
    Попробуйте посчитать вычислительную сложность приведённого алгоритма. 
    Что будет, если сгенерировать массив данных длиной 10^5 элементов и запустить алгоритм на нём? 
    Подсказка: задачу можно решить за количество операций O(n).
    """
    count_array = [0 for i in range(k)]
    for elm in subset_values:
        count_array[elm % k] += 1
    if k % 2 == 0:
        count_array[k // 2] = min(count_array[k // 2], 1)
    result = min(count_array[0], 1)
    for i in range(1, (k // 2) + 1):
        result += max(count_array[i], count_array[k - 1])

    # getting input number
    link_num = "".join(filter(str.isdigit, input_link))
    file = open("output/output" + link_num + ".txt", "w")
    file.write(result.__str__())
    file.close()
    return

"""
def count_occurrences(current_num, subset_values, subset_stats):
    occurrences = 0
    for elm in subset_values:
        # skipping first elm
        if current_num != elm:
            permutation = current_num + elm
            # print(str(int(current_num)) + "+" + str(int(elm)) + "=" + str(permutation))
            if permutation % subset_stats[1] == 0:
                occurrences += 1
                # print([current_num, occurrences])
    return [current_num, occurrences]


def check_max_occurrences(subset_values, subset_stats):
    max_occurrences = [0, 0]
    for elm in subset_values:
        occurrences = count_occurrences(elm, subset_values, subset_stats)
        if max_occurrences[1] < occurrences[1]:
            max_occurrences = occurrences
    return max_occurrences
"""

init()
