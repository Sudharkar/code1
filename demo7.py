import pandas as pd
print(pd.__version__)
data={
    "Name":["ram","shyam","ambani","sunita","manoj","hanuman"],
    "Age":[45,66,54,45,34,500],
    "City":["indore","pune","baglore","Hydrabad","mumbai","bharat"]
}
df=pd.DataFrame(data)
#print(df)
'''
print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(2))
df.to_csv("output.csv")
df.to_excel("output.xlsx")

df.to_json("output.json")
'''
print(df.info())
