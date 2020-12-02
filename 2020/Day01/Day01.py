from inspect import getsourcefile
from pathlib import Path

input_file = Path(getsourcefile(lambda:0)).resolve().parent.joinpath('ExpenseReport.txt')

with open(input_file) as expense_report:
    expense_list = [int(expense) for expense in expense_report]
    expense_list.sort()
    small_index = 0
    large_index = len(expense_list) - 1

    found_indices = False
    while not found_indices:
        expense_sum = expense_list[small_index] + expense_list[large_index]
        if expense_sum == 2020:
            found_indices = True
        elif expense_sum > 2020:
            large_index = large_index - 1
        else:  # expense_sum < 2020
            small_index = small_index + 1

    print('small = ' + str(expense_list[small_index]))
    print('large = ' + str(expense_list[large_index]))
    print('product - 2 = ' + str(expense_list[small_index] * expense_list[large_index]))

    found_tri_indices = False
    index_0 = 0
    index_1 = 1
    index_2 = 2
    tri_sum = 0
    while not found_tri_indices:
        while not found_tri_indices:
            while not found_tri_indices:
                tri_sum = expense_list[index_0] + expense_list[index_1] + expense_list[index_2]
                if tri_sum == 2020:
                    found_tri_indices = True
                elif tri_sum < 2020:
                    index_2 = index_2 + 1
                else:  # tri_sum > 2020
                    break
            if not found_tri_indices:
                index_1 = index_1 + 1
                index_2 = index_1 + 1
            tri_sum = expense_list[index_0] + expense_list[index_1] + expense_list[index_2]
            if tri_sum > 2020:
                break
        if not found_tri_indices:
            index_0 = index_0 + 1
            index_1 = index_0 + 1
            index_2 = index_1 + 1

    print('@index_0 = ' + str(expense_list[index_0]))
    print('@index_1 = ' + str(expense_list[index_1]))
    print('@index_2 = ' + str(expense_list[index_2]))
    print('product - 3 = ' + str(expense_list[index_0] * expense_list[index_1] * expense_list[index_2]))
