import os

Atheris_dir = "./Atheris/Results/"
FreeFuzz_dir = "./FreeFuzz/Results/"

def get_info(cur_dir,filename):
    """get file number,stats_covered,stats_miss in file

    Args:
        cur_dir (string): dir to work
        filename (string): filename
    """
    with open(cur_dir+filename) as f:
        contents = f.readlines()
        file_nums = len(contents) -4
        info_need = contents[-1].split()
        stats_covered = info_need[-3]
        stats_miss = info_need[-2]
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
        f.write("===============================================================\n")
        f.write(key.ljust(max_width+3)+ " | files Cov | " + "stats Cov | " + "stats Miss |" + "\n")
        f.write("---------------------------------------------------------------\n")
        for value_in in value:
            f.write(value_in[0].ljust(max_width+6) + value_in[1].ljust(9+3) + value_in[2].ljust(9+3) + value_in[3].ljust(10+2) + "\n")
    f.close()

def main():
    results ={}
    add_results(results,Atheris_dir,"Atheris")
    add_results(results,FreeFuzz_dir,"FreeFuzz")
    write_results(results)

if __name__ == "__main__":
    main()