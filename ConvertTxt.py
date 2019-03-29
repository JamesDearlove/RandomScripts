import os
for filename in os.listdir('raw'):
    with open("raw/" + filename, "r") as group_data, \
        open(filename, "w") as clean_data:
        for line in group_data:
            username = line.split(",")[0][4:]
            clean_data.write(username + "\n")