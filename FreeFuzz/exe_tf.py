RES_KEY = "results"
RESULT_KEY = "res"
ERROR_KEY = "err"
ERR_ARG_KEY = "error_args"
ERR_CPU_KEY = "err_cpu"
ERR_GPU_KEY = "err_gpu"
RES_CPU_KEY = "res_cpu"
RES_GPU_KEY = "res_gpu"
ERR_HIGH_KEY = "err_high"
ERR_LOW_KEY = "err_low"
RES_HIGH_KEY = "res_high"
RES_LOW_KEY = "res_low"
TIME_LOW_KEY = "time_low"
TIME_HIGH_KEY = "time_high"

current_dir = "/home/usr/FreeFuzz/src/tf-output/crash-oracle/success"

import argparse
import os,glob

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fc","--func",help="function_name to run")
    parser.add_argument("-f","--file",help="file contains function names")
    return parser

def insert_code(file,line):
    with open(file,"r+") as f:
        content = f.read()
        f.seek(0,0)
        if content[0] == 'R':
            return
        f.write(line.rstrip('\r\n') + '\n' + content)

def run_func(name):
    def_code = """RES_KEY = "results"
RESULT_KEY = "res"
ERROR_KEY = "err"
ERR_ARG_KEY = "error_args"
ERR_CPU_KEY = "err_cpu"
ERR_GPU_KEY = "err_gpu"
RES_CPU_KEY = "res_cpu"
RES_GPU_KEY = "res_gpu"
ERR_HIGH_KEY = "err_high"
ERR_LOW_KEY = "err_low"
RES_HIGH_KEY = "res_high"
RES_LOW_KEY = "res_low"
TIME_LOW_KEY = "time_low"
TIME_HIGH_KEY = "time_high"
results = dict()
results[ERR_CPU_KEY] = None
results[ERR_GPU_KEY] = None
results[ERR_HIGH_KEY] = None
results[ERR_LOW_KEY] = None"""

    number_test = 0
    print(name)
    files_list = []
    for file in os.listdir(current_dir):
        if file.startswith(name+"-") and file.endswith(".py"):
            number_test += 1
            insert_code(file,def_code)
            files_list.append(file)

    print("Complete!")
    if number_test == 0:
        return
    #os.system("coverage erase")
    i =0
    for file in files_list:
        i +=1
        if i == 1:
            os.system("python3 -m coverage run -L --source=/usr/local/lib/python3.8/dist-packages/tensorflow/ "+ file)
        else:
            os.system("python3 -m coverage run -a -L --source=/usr/local/lib/python3.8/dist-packages/tensorflow/ "+ file)
    print("Number of tests: ",end="")
    print(number_test)
    #os.system("python3 -m coverage report --include=/usr/local/lib/python3.8/dist-packages/tensorflow/*.py > " + name +".coverage")

def run_file(filename):
    func_list = []
    with open(filename,"r") as f:
        for lines in f.readlines():
            line = lines.strip("\n")
            func_list.append(line)
    for func in func_list:
        run_func(func)
    os.system("python3 -m coverage report --include=/usr/local/lib/python3.8/dist-packages/tensorflow/*.py > total.coverage")

def main():
    parser = init_parser()
    args = parser.parse_args()
    if args.func:
        run_func(args.func)
    elif args.file:
        run_file(args.file)

if __name__ == "__main__":
    main()

