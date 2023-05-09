'''if i[0]=='':
                continue
            elif i[0] == "+":
                continue
            else:
                print(a,".",i,sep="")
                a+=1
#questions()    '''
import csv
csv.register_dialect("plus",delimiter=",",skipinitialspace=True)
def questions():
    datum=[[]]
    num=0
    a=1
    with open("Questions.txt","r") as rf:
        data=csv.reader(rf,dialect="plus")
        #print(list(data))
        for i in data:
            #print(i)
            if i[0]=="+":
                datum.append([])
                num+=1
                continue
            datum[num].append(i[0])
                #datum.append(i[0].rstrip(","))
    return datum
def printf(datum1,datum2):
    a=1
    abc=0
    total=0
    for i in datum2:
        if len(i)>1:
            for j in i:
                print(a,".",chr(65+abc),".",i[abc],sep="")
                abc+=1
                total+=1
                break
            abc=0
            a+=1
            continue
        print(a,".",i[0],sep="")
        a+=1
        total+=1
    print("Total:",total)

def answers():
    a=1
    datum=[[]]
    num=0
    last=0
    #datum=open("Answers.txt","r",encoding="utf-8")
    csv.register_dialect("s",delimiter="+",skipinitialspace=True)
    with open("Answers.txt","r",encoding="utf-8") as rf:
        data=csv.reader(rf,dialect="plus")
        for i in data:

            #print("\n\n",i)
            if i[0]=="+":
                last=0
                datum.append([])
                num+=1
                continue
            datum[num].append("".join([str(x)+" " for x in i]))
            #print(a,datum[num],sep="")
            if last==0:
                a+=1
                last=1
    return datum
def runner():
	ques=questions()
	ans=answers()
	return ques,ans
'''num=1
for i in range(len(ans)):
    print("Number:",num)
    print("Question:",ques[i])
    print("Answer:",ans[i])
    print("\n")
    num+=1'''
#printf(questions(),answers())
