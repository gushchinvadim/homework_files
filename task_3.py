path = "three/"
file_names = ["1.txt", "2.txt"]

files_info = []

for file_name in file_names:
    with open(path+file_name, "r") as file:
        count_lines = 0
        while file.readline():
            count_lines += 1
        files_info.append({"file_name": file_name, "count_lines": count_lines})

files_info.sort(key=lambda x: x["count_lines"])

with open(path + "3.txt", "w") as main_file:
    for file_info in files_info:
        with open(path+file_info["file_name"]) as some_file:
            main_file.write(file_info["file_name"] + "\n")
            main_file.write(str(file_info["count_lines"]) + "\n")

            line = some_file.readline()
            while line:
                main_file.write(line.strip() + "\n")
                line = some_file.readline()
