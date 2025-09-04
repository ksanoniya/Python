import pandas as pd

data = ([1,"kalash","sanoniya","khategaon"],
        [2,"suyash","sanoniya","indore"],
        [3,'harsh','yadav','mumbai'])
df = pd.DataFrame(data,columns=['id','name','last_name','city'])
# print(df)

data2 = {
    "name" : ["kalash","yash","raj","abhayraj"],
    "age"  : [20,30,40,10],
    "city" : ["khategaon","indore","mumbai"," "]
}

dt2 = pd.DataFrame(data2)
# print(dt2)
df.to_csv("data.csv",index=False)
df.to_json("data.json")
df.to_excel("data.xlsx")
readd = pd.read_csv("data.csv")     

print(readd)