import random
def random_pick(the_list:list,random_num:int):
    return random.sample(the_list, random_num)

if __name__ == "__main__":
    f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/api_list.txt")
    random_api_list = random_pick(f.readlines(),50)
    f.close()
    f = open("/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/random_api_list_50.txt","w")
    for i in sorted(random_api_list):
        f.write(i)
    f.close()