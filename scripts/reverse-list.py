#!/usr/bin/python3

print("Problem: Reverse a list without built-in function")
original_list = [1,2,3,4,5]

count = len(original_list) - 1

result_list = []
while count >= 0:
    result_list.append(original_list[count])
    count -= 1
else:
    print("Soemthing went wrong")

print(original_list, result_list)