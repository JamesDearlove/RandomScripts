import os

with open("groups.txt", "r") as group_data:
    for line in group_data:
        group_name = line.split(",")[0][4:]
        command = f'dsquery group -name "{group_name}" | dsget group -members > "{group_name}.txt"'
        os.system(command)