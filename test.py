import re

file_path = 'C:/Users/DrillSergeant/Desktop/gupdate-exec-chbrowser.log'
f = open(file_path)
content = f.readlines()
content.reverse()
result_list = []
count = 0
for line in content:
    if "eid:" in line:
        result_list.append(line)
        count += 1
        if count == 2:
            break
formatted_list = [value.split('eid: ')[1] for value in result_list]
for value in formatted_list:
    print(value)
dict_1 = {pair.split(".")[0]: pair.split(".")[1] for pair in formatted_list[0].split(";")}
dict_2 = {pair.split(".")[0]: pair.split(".")[1] for pair in formatted_list[1].split(";")}

print("Dictionary 1:", dict_1)
print("Dictionary 2:", dict_2)


def find_differences():
    differences_ = {key_: (dict_1.get(key_), dict_2.get(key_)) for key_ in set(dict_1) | set(dict_2)}
    return differences_


value1 = formatted_list[0]
value2 = formatted_list[1]
differences = find_differences()
print(differences)
for key, values in differences.items():
    if values[0] != values[1]:
        print(f"{key}: {values[0]} first dict, {values[1]} во втором словаре")
