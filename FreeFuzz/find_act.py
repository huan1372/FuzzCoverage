import os
current_dir = "/home/usr/FreeFuzz/src/tf-output/crash-oracle/success"
def check_files(name):
    for file in os.listdir(current_dir):
        if file.startswith(name+"-") and file.endswith(".py"):
            return True
output_file = "/home/usr/FreeFuzz/src/tf-output/crash-oracle/success/cleaned_api"

outf = open(output_file,"w")
with open("api_list.txt") as f:
    for lines in f.readlines():
        line = lines.strip("\n")
        if check_files(line):
            outf.write(lines)
