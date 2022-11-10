import os
def run_Atheris(func_name,file_path,coverage_path,atheris_run,coverage=True):
    import time
    t1 = time.time()
    str_a = "python3 -m coverage run -L --source=/usr/local/lib/python3.8/dist-packages/tensorflow " + file_path + func_name + "_fuzz.py -rss_limit_mb=8192 -atheris_runs=" + atheris_run
    print(str_a)
    os.system(str_a)
    if coverage == True:
        os.system("python3 -m coverage report -m --include=/usr/local/lib/python3.8/dist-packages/tensorflow/*.py > " + coverage_path + func_name + "_1000.Coverage")
    t2 = time.time()
    print(t2-t1)
    return

def run_all_Atheris(func_name,file_path,atheris_run):
    str_a = "python3 -m coverage run -a -L --source=/usr/local/lib/python3.8/dist-packages/tensorflow " + file_path + func_name + "_fuzz.py -rss_limit_mb=8192 -atheris_runs=" + atheris_run
    print(str_a)
    os.system(str_a)
    return

if __name__ == "__main__":
    output_folder = "/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/"
    file_path = output_folder + "Tests/"
    with open('/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/random_api_list_50_remain.txt') as f:
        for i in f.readlines():
            api_name = i.rstrip()
            run_all_Atheris(func_name=api_name,file_path=file_path,atheris_run="2000")
    os.system("python3 -m coverage report -m --include=/usr/local/lib/python3.8/dist-packages/tensorflow/*.py > " + coverage_path + func_name + "_1000.Coverage")
    run_all_Atheris