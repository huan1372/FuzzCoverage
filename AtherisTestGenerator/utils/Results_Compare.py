Atheris_dir = "/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/CovReport/"
FreeFuzz_dir = "/home/usr/FreeFuzz/FuzzCoverage/FreeFuzz/Results/"

def process_line(AtherisContent,FreeFuzzContent):
    lineA = AtherisContent.split()
    lineF = FreeFuzzContent.split()
    filename = lineA[0]
    if filename != lineF[0] or lineA[1]!=lineF[1]:
        raise Exception("Filename not matched")
    filename = filename[39:]
    LineCompare = int(lineF[2]) - int(lineA[2])
    setA = set([j.strip(",") for j in lineA[4:]])
    setF = set([j.strip(",") for j in lineF[4:]])
    return filename,str(LineCompare),str(setA - setF),str(setF - setA),str(setA.intersection(setF))
def Compare_Result(api_name,Atheris_dir,FreeFuzz_dir,output_dir="/home/usr/FreeFuzz/FuzzCoverage/AtherisFuzzer/Comparison/"):
    output_f = open(output_dir+api_name+".Compare","w")
    Atheris_f = open(Atheris_dir+api_name+"_1000.Coverage")
    FreeFuzz_f = open(FreeFuzz_dir+api_name+".Coverage")
    Atheris_content = Atheris_f.readlines()
    FreeFuzz_content = FreeFuzz_f.readlines()
    diff = 0
    lineNum = 0
    output_f.write("FileName                                                      | CoverDiff | " + "AtherisMiss                                                                                          | " + "FreeFuzzMiss                                                                                         | " + "MutualMiss                                   |"+"\n")
    for i in range(len(Atheris_content)):
        if Atheris_content[i].startswith("TOTAL"):
            break
        if Atheris_content[i] != FreeFuzz_content[i]:
            diff+=1
            filename,lineComp,AtherisMiss,FreeFuzzMiss,MutualMiss = process_line(AtherisContent=Atheris_content[i],FreeFuzzContent=FreeFuzz_content[i])
            lineNum += int(lineComp)
            output_f.write(filename.ljust(64) + lineComp.ljust(9+3) + AtherisMiss.ljust(100+3) + FreeFuzzMiss.ljust(100+3) + MutualMiss.ljust(100+2) + "\n")
    output_f.write("TOTAL DIFFERENCE in LINES: " + str(lineNum) +"\n")
    print(diff)
    return


def main():
    api_name = "tf.abs"
    Compare_Result(api_name,Atheris_dir=Atheris_dir,FreeFuzz_dir=FreeFuzz_dir)
if __name__ == "__main__":
    main()