import os
def run_Atheris(func_name,file_path,coverage_path,coverage=True):
    import time
    t1 = time.time()
    str_a = "python3 -m coverage run -L --source=/usr/local/lib/python3.8/dist-packages/tensorflow " + file_path + func_name + "_fuzz.py -atheris_runs=10000"
    print(str_a)
    os.system(str_a)
    if coverage == True:
        os.system("python3 -m coverage report --include=/usr/local/lib/python3.8/dist-packages/tensorflow/*.py > " + coverage_path + func_name + "_1000.Coverage")
    t2 = time.time()
    print(t2-t1)
    return