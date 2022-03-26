
def multi_list(lst):
    if len(lst) == 0:
        return 0
    product = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            product = product * i
    return product

print(multi_list([3,3,3]))
print(multi_list([0, 2 ,6]))

