list_signs = ['*', '*', '*', '*', '*']
length_list_signs = len(list_signs)
index_signs = 1
for index_list in list_signs:
    signs = index_list * index_signs
    print(signs)
    index_signs += 1
    if index_signs == length_list_signs:
        for index_list_ in list_signs:
            num = index_list_ * index_signs
            index_signs -= 1
            print(num)