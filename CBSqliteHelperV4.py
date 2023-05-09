import sqlite3
import random as r
from helper import runner
import csv
covid=sqlite3.connect("Covid19.db",check_same_thread=False)
cur=covid.cursor()

def train2():
    csv.register_dialect("Sep",delimiter=":",skipinitialspace=True)
    data=[]
    k=0
    with open("Key&Res.txt","r") as f:
        data=csv.reader(f,dialect="Sep")
        for i in data:
            k+=1
            id,response=i[0],i[1]
            print(f"The input is {id} and the response is {response}")
            print(k)
            cur.execute("INSERT INTO Responses (KW1,KW2,KW3,RS) VALUES (?,?,?,?);",(id,id,id,response))
        covid.commit()
        f.close()
def train():
    keys,ans=keyword()
    for i in range(len(keys)-1):
        print(i,keys[i])
        cmd="Select * from Responses"
        if len(keys[i])==1:
            cur.execute("Insert into Responses(KW1,KW2,KW3,RS) Values (?,?,?,?)",(keys[i][0],keys[i][0],keys[i][0],ans[i][0]))        
        elif len(keys[i])==2:
            cur.execute("Insert into Responses(KW1,KW2,KW3,RS) Values (?,?,?,?)",(keys[i][0],keys[i][1],keys[i][0],ans[i][0]))
        elif len(keys[i])>=3:
            cur.execute("Insert into Responses(KW1,KW2,KW3,RS) Values (?,?,?,?)",(keys[i][0],keys[i][1],keys[i][2],ans[i][0]))
        #try:
    #   cur.execute(cmd)
        #except sqlite3.OperationalError:
            
    #   print("\nthis troubles me",ans[i][0],"\n\n")
#   cur.execute(cmd)
    covid.commit()


#This function trains the bot on what response to give for a query

#This function finds what the keywords are in the given input
def keyword(query="qwerty"):
    if query=="qwerty":
        question=runner()[0]
        answer=runner()[1]
        num="break"
        word=[]
        words=[]
        for i in question:
            if type(i)==list:
                for j in i:
                    h=j.rstrip("?") 
                    words.append(h)
            else:
                h=i.rstrip("?") 
                words.append(h)
            words.append(num)
        #print(*words,sep="\n      ")
        for i in words:
            w=i.split(" ")
            word.extend(w)
        #setw=set(word)
        # print(*word,sep="\n     ")
        sentence=[[]]
        hit=False
        cov=False
        a=0
        ignore=["the","it","is","can","about","are","for","from","does","did","i","was","were","am","be","has","have","had","do","will","shall","could","would","may","might","must","you","to","your","a","on","my","if","get","in","as","takes","take","like","with"]
        covids=["covid","covid-19","covid-","19","covid19","corona","coronavirus","virus"]
        questions=["what","where","when","why","how","who","which"]
        for i in word:
            hit=False
            if i=="break":
                sentence.append([])
                a+=1
                #print("This is done")
                continue
            elif i=="":
                hit=True
                #continue
            elif( i.lower() in ignore):
                hit=True
            elif(i.lower() in questions):
                hit=True
            elif(i.lower() in covids):
                hit=True
            elif i.lower() in sentence[a]:
                hit=True
                #continue
            if hit==True:
                if cov==False:
                    sentence[a].append("covid")
                    cov=True
            #print("i is",i.lower(),"Ignored")
                continue
            else:
                sentence[a].append(i.lower())
                pass
                #print("i is",i.lower())    
            pass
        '''for i in sentence:
        if len(i)==0:
            sentence.remove(i)'''
        for i in range(len(answer)):
        #print("Question:",question[i])
    #   print("Answer:",answer[i])
            print(i,"Keyword:",sentence[i])
        #print("\n")
            pass
    #print("Total Questions:",len(question))
    #print("Total Keywords:",len(sentence))
  #  print("Total Answers:",len(answer))    #This function returns the response
        return sentence,answer
    else:
        check=query.split(" ")
        word=[]
        words=[]
        for i in check:
            h=i.rstrip("?") 
            words.append(h)
        print(*words,sep="\n      ")
        for i in words:
            w=i.split(" ")
            word.extend(w)
        #setw=set(word)
        # print(*word,sep="\n     ")
        sentence=[[]]
        hit=False
        cov=False
        a=0
        ignore=["it","is","can","about","are","for","from","does","did","i","was","were","am","be","has","have","had","do","will","shall","could","would","may","might","must","you","to","your","a","on","my","if","get","in","as","takes","take","like","with"]
        covids=["covid","covid-19","covid-","19","covid19","corona","coronavirus","virus"]
        questions=[]#["what","where","when","why","how","who","which"]
        for i in word:
            hit=False
            if i=="break":
                sentence.append([])
                a+=1
                continue
            elif i=="":
                hit=True
            elif( i.lower() in ignore):
                hit=True
            elif(i.lower() in questions):
                hit=True
                cov=False
            elif(i.lower() in covids):
                hit=True
            elif i.lower() in sentence[a]:
                hit=True
            if hit==True:
                if cov==False:
                    sentence[a].append("covid")
                    cov=True
                continue
            else:
                sentence[a].append(i.lower())
        return sentence                 



greetings=["hi","hello","hey","aisha"]
who=["who","what","you"]


def give_res(query):
    keywords=keyword(query)
    user=query
    if query[len(query)-1]=="?":
        user=query.rstrip("?")
    word=user.split(" ")
    words=[i.lower() for i in word]
    print("words:",words)
    print("keywords:",keywords)
    responses={"all":"sorry"}
    toadd=0
    for i in range(len(keywords[0])):    
            current=keywords[0][i]        
            print(i)
            cur.execute(f"select RS from Responses where KW1='{current.lower()}'")
            toadd=cur.fetchall()
            if (len(toadd)>0):
                responses[current]=toadd[0][0]
            cur.execute(f"select RS from Responses where KW2='{current.lower()}'")
            toadd=cur.fetchall()
            if (len(toadd)>0):
                responses[current]=toadd[0][0]
            cur.execute(f"select RS from Responses where KW3='{current.lower()}'")
            toadd=cur.fetchall()
            if (len(toadd)>0):
                responses[current]=(toadd)[0][0]
    #            print("\n\n3.Responses are:",responses)
##    if len(responses[0])>1:
##        responses.pop(0)
    print(responses)
    dict_keys=list(responses.keys())
    answer=list(responses.values())
    if len(answer)>2:
    	while ("covid" in dict_keys):
            index=dict_keys.index("covid")
            dict_keys.pop(index)
            answer.pop(index)
    else:
        pass
    #answer=list(set(answer))
    print("\n\n\nanswer is")
    print(*answer,sep="\n\n             ")
    best={}
    bestans=[]
    if len(answer)>1:
        answer.remove("sorry")
    for i in answer:
        if i not in best.keys():
            best[i]=answer.count(i)
    print("the best answers:",best)
    highcount=0
    high_key=[]
    for i in best.keys():
        if best[i]>highcount:
            highcount=best[i]
            high_key=i
    bestans=high_key
    return bestans
#for i in range(5):
   #print("bot:",give_res(input("You:")))
#keyword()
#train()
first=(False)
if first==True:
    cmd="""Drop Table Responses"""
    cur.execute(cmd)
    cmd="""CREATE TABLE Responses(
KW1 varCHAR(100),
KW2 varCHAR(100),
KW3 varCHAR(100),
RS varCHAR(9000)
)"""
    cur.execute(cmd)
    print("done")
    train()
    train2()
else:
    print("exists")
#train2()