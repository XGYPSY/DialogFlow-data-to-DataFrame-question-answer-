df=pd.DataFrame({"question":[],"answer":[]},index=None)
import json
import os
path="/root/Downloads/EcommerceBot/intents/"
files=sorted(os.listdir(path))
qst=[]
ans=[]
for i in range(0,len(files),2):
    qst.append(files[i+1])
    ans.append(files[i])
questions=[]
answers=[]
for it1,it2 in zip(qst,ans):
    f=open(path+it2)
    data=json.load(f)
    ans=""
    for it in data["responses"]:
        for its in it["messages"]:
            if "speech" not in its:
                ans=its["textToSpeech"]
            else:
                ans=its["speech"]
    if len(ans)==0:
        ans="Didn't get that please contact privately"
    else:
        ans=ans.replace("{","").replace("}","").replace("$","")
        ans.replace("url","url")
        if ans.find("<")>0:
            ans="Visit https://mydreamstore.in/"
    f=open(path+it1)
    data=json.load(f)
    for it in data:
        ques=""
        for its in it["data"]:
            ques+=its["text"]
        questions.append(ques)
        answers.append(ans)
df=df.append(pd.DataFrame({"question":questions,"answer":answers}))
