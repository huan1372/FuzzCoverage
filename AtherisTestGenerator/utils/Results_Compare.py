Atheris_dir = "/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/CovReport/"
FreeFuzz_dir = "/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/FreeFuzzCovReport/"

def Find_all_line(ListR:list):
    Line_number = []
    for i in ListR:
        if "-" in i:
            number = i.split("-")
            for j in range(int(number[0]),int(number[1])+1):
                Line_number.append(j)
        else:
            Line_number.append(int(i))
    return Line_number

def convertbackline(setR):
    if len(setR) == 0:
        return ""
    list_number = sorted(list(setR))
    if len(list_number) == 1:
        return str(list_number[0])
    start = list_number[0]
    prev_i = None
    outputL = []
    for i in list_number:
        if prev_i != None:
            if i != prev_i+1:
                if start == prev_i:
                    outputL.append(str(start))
                else:
                    outputL.append(str(start)+"-"+str(prev_i))
                start = i
        prev_i = i
    if start == i:
        outputL.append(str(start))
    else:
        outputL.append(str(start)+"-"+str(prev_i))

    return " ,".join(outputL)

def process_line(AtherisContent,FreeFuzzContent):
    lineA = AtherisContent.strip().split()
    lineF = FreeFuzzContent.strip().split()
    filename = lineA[0]
    if filename != lineF[0] or lineA[1]!=lineF[1]:
        raise Exception("Filename not matched")
    filename = filename[39:]
    LineCompare = str(int(lineF[2]) - int(lineA[2]))
    lineACov = str(int(lineA[1]) - int(lineA[2]))
    lineFCov = str(int(lineF[1]) - int(lineF[2]))
    #LineCompare += "(" + lineACov + "/" + lineFCov + ")"
    setA = set(Find_all_line([j.strip(",") for j in lineA[4:]]))
    setF = set(Find_all_line([j.strip(",") for j in lineF[4:]]))
    #print(setA-setF)
    return filename,LineCompare,convertbackline(setA - setF),convertbackline(setF - setA),convertbackline(setA.intersection(setF))

def merge_line(f1Content,f2Content):
    line1 = f1Content.split()
    line2 = f2Content.split()
    filename = line1[0]
    if filename != line2[0] or line1[1]!=line2[1]:
        raise Exception("Filename not matched")
    #filename = filename[39:]
    Total_Stats = int(line1[1])
    Miss = len(setA.intersection(setF))
    Cov = str(int((Total_Stats-Miss)/Total_Stats*100)) + "%"
    return filename.ljust(100) + str(Total_Stats).rjust(6) + str(Miss).rjust(5) + Cov.rjust(6) + convertbackline(setA.intersection(setF)) + "\n"
def Compare_Result(api_name,Atheris_dir,FreeFuzz_dir,output_dir="/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Comparison/"):
    print(api_name)
    output_f = open(output_dir+api_name+".Compare","w")
    Atheris_f = open(Atheris_dir+api_name+"_1000.Coverage")
    FreeFuzz_f = open(FreeFuzz_dir+api_name+".Coverage")
    Atheris_content = Atheris_f.readlines()
    FreeFuzz_content = FreeFuzz_f.readlines()
    diff = 0
    lineNum = 0
    Total_Cov_F = "0"
    Total_Cov_A = "0"
    output_f.write("FileName                                                      | CoverDiff | " + "AtherisMiss                                                                                          | " + "FreeFuzzMiss                                                                                         | " + "MutualMiss                                   |"+"\n")
    for i in range(len(Atheris_content)):
        if Atheris_content[i].startswith("TOTAL"):
            Total_Cov_line_A = Atheris_content[i].strip().split()
            Total_Cov_A = str(int(Total_Cov_line_A[1])-int(Total_Cov_line_A[2]))
            Total_Cov_line_F = FreeFuzz_content[i].strip().split()
            Total_Cov_F = str(int(Total_Cov_line_F[1])-int(Total_Cov_line_F[2]))
            break
        if Atheris_content[i] != FreeFuzz_content[i]:
            diff+=1
            filename,lineComp,AtherisMiss,FreeFuzzMiss,MutualMiss = process_line(AtherisContent=Atheris_content[i],FreeFuzzContent=FreeFuzz_content[i])
            lineNum += int(lineComp)
            output_f.write(filename.ljust(64) + lineComp.ljust(9+3) + AtherisMiss.ljust(100+3) + FreeFuzzMiss.ljust(100+3) + MutualMiss.ljust(100+2) + "\n")
    output_f.write("\nTOTAL DIFFERENCE in LINES: " + str(lineNum) +"\n")
    output_f.write("TOTAL Coverage for Atheris for API(" + api_name + ") in LINES: " + Total_Cov_A +"\n")
    output_f.write("TOTAL Coverage for FreeFuzz for API(" + api_name + ") in LINES: " + Total_Cov_F +"\n")
    print(diff)
    output_f.close()
    Atheris_f.close()
    FreeFuzz_f.close()
    return

def merge_result(file1,file2,out_f):
    results = []
    f1 = open(file1,"r")
    f2 = open(file2,"r")
    f3 = open(out_f,"w")
    f1_content =f1.readlines()
    f2_content = f2.readlines()
    f1.close()
    f2.close()
    if len(f1_content) != len(f2_content):
        raise Exception("NOT same length")
    for i in range(len(f1_content)):
        if f1_content[i].startswith("Name") or f1_content[i].startswith("----------------"):
            f3.write(f1_content[i])
        else:
            if f1_content[i] != f2_content[i]:
                f3.write(merge_line(f1_content[i],f2_content[i]))
            else:
                f3.write(f1_content[i])
    return results
def main():
    with open("/home/usr/FreeFuzz/FuzzCoverage/AtherisTestGenerator/random_api_list_50.txt") as f:
        for line in f.readlines():
            api_name = line.strip("\n")
            Compare_Result(api_name,Atheris_dir=Atheris_dir,FreeFuzz_dir=FreeFuzz_dir)

if __name__ == "__main__":
    main()