def ValuetoIndex(list, NewValue):
    if NewValue in list:
        index = list.index(NewValue)
    else:
        list.append(NewValue)
        index = list.index(NewValue)
    return list, index

list = ["aa", "ee", "zz"]
print(list)


NewValue = input("New value: ")
updated_list, index = ValuetoIndex(list, NewValue)
sortList = sorted(updated_list)
Newindex = sortList.index(NewValue)
print("List after sort", sortList)
print("Index =", Newindex)