import os
import argparse
import FreeFuzz.exe_tf as extf

Atheris_dir = "./Atheris/Results/"
FreeFuzz_dir = "./FreeFuzz/Results/"
Atheris_fuzzer_dir = "/home/usr/FreeFuzz/FuzzCoverage/Atheris/Tests/"

Time = {"tf.abs":["300","289"],"tf.math.sqrt":["","2640"]}
def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fc","--func",help="generate coverage report for FreeFuzz with function name")
    parser.add_argument("-f","--file",help="file contains function names")
    parser.add_argument("-gr","--genreport",help="generate report based on .Coverage")
    parser.add_argument("-Afc","--AtherisFunc",help="Generate fun")
    return parser

def get_info(cur_dir,filename):
    """get file number,stats_covered,stats_miss in file

    Args:
        cur_dir (string): dir to work
        filename (string): filename
    """
    stats_covered = 0
    stats_miss = 0
    file_nums = 0
    with open(cur_dir+filename) as f:
        f.readline()
        f.readline()
        for i in f.readlines():
            if i.startswith("----"):
                break
            line = i.split()
            stats = int(line[-3])
            miss = int(line[-2])
            stats_covered += stats
            stats_miss += miss
            file_nums +=1
            if (stats == miss) and (line[-1]=="0%"):
                file_nums -= 1
                stats_covered -= stats
                stats_miss -= miss
    return file_nums,stats_covered,stats_miss

def add_results(results,cur_dir,tool):
    """Add results of the coverage running in following directory

    Args:
        results (dict): variable to store results
        cur_dir (string): current directory
        tool (string): tools that coverage.py examine
    """
    for file in os.listdir(cur_dir):
        if file.endswith("_1000.Coverage"):
            name = file[:-14]
            file_num,stats_covered,stats_miss = get_info(cur_dir,file)
            if name not in results.keys():
                results[name] = [(tool,str(file_num),str(stats_covered),str(stats_miss))]
            else:
                results[name].append((tool,str(file_num),str(stats_covered),str(stats_miss)))

def write_results(results):
    f = open("results.txt","w")
    max_width = max(len(i) for i in results.keys())
    for key,value in results.items():
        f.write("====================================================================================\n")
        f.write(key.ljust(max_width+3)+ " | files Cov | " + "stats Tot | " + "stats Miss | " + "Time |"+"\n")
        f.write("------------------------------------------------------------------------------------\n")
        for value_in in value:
            if key in Time.keys():
                if value_in[0] == "Atheris":
                    time_info = Time[key][0]
                else:
                    time_info = Time[key][1]
            else:
                time_info = ""
            f.write(value_in[0].ljust(max_width+6) + value_in[1].ljust(9+3) + value_in[2].ljust(9+3) + value_in[3].ljust(10+3) + time_info.ljust(4+2) + "\n")
    f.close()

def generate_report():
    """function to generate report
    """
    results ={}
    add_results(results,Atheris_dir,"Atheris")
    add_results(results,FreeFuzz_dir,"FreeFuzz")
    write_results(results)
    return results

def run_Atheris(func):
    for file in os.listdir(Atheris_fuzzer_dir):
        print(file)
        if file.startswith(func) and file.endswith("_fuzz.py"):
            os.system("python3 -m coverage run -L --source=/usr/local/lib/python3.8/dist-packages/tensorflow " + Atheris_fuzzer_dir + file + " -atheris_runs=10000")
            os.system("python3 -m coverage report -m --include=/usr/local/lib/python3.8/dist-packages/tensorflow/*.py > " + "./Atheris/Results/" + func + "_1000.Coverage")
            break
def run_all_Atheris():
    for file in os.listdir(Atheris_fuzzer_dir):
        if file.startswith(func) and file.endswith("_fuzz.py"):
            os.system("python3 -m coverage run -L --source=/usr/local/lib/python3.8/dist-packages/tensorflow " + Atheris_fuzzer_dir + file + " -atheris_runs=20000")
            os.system("python3 -m coverage report -m --include=/usr/local/lib/python3.8/dist-packages/tensorflow/*.py > " + "./Atheris/Results/" + func + "_1000.Coverage")
            break
def main():
    parser = init_parser()
    args = parser.parse_args()
    if args.func:
        extf.run_func(args.func)
    elif args.file:
        extf.run_file(args.file)

    if args.AtherisFunc:
        run_Atheris(args.AtherisFunc)
    if args.genreport:
        generate_report()

if __name__ == "__main__":
    main()