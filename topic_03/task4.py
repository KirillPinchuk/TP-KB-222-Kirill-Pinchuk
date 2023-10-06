def InsterToPosition(sorted_list, NewValue):
    position = 0
    for i in sorted_list:
     if NewValue < i:
      position +=1
     return position
list = ["aa", "ee", "zz"]  
NewValue = input("New value: ")
insert_position = InsterToPosition(list, NewValue)
list.insert(insert_position, NewValue)
print(f"position: {insert_position}, list: {list}")