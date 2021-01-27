from argparse import ArgumentParser
parser=ArgumentParser()
parser.add_argument("inputfile",help="input filename")
args=parser.parse_args()
inputfile=args.inputfile

def research(dict_,num):
    l=[]
    s=""
    for i in dict_.keys():
        if num%i==0:
            l.append(i)
    l.sort()
    for i in l:
        s+=dict_[i]
    return s if not s=="" else num

def main():
    n_w_dict={}
    num=0
    with open(inputfile) as f:
        for st in f:
            st=st.rstrip("\n")
            if ":" in st:
                n_w_dict[int(st.split(":")[0])]=st.split(":")[1]
            else:
                num=st
        print(research(n_w_dict,int(num)))

if __name__=="__main__":
    main()