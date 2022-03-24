import pandas


getcsv=pandas.read_csv("my_csv.csv")
df=pandas.DataFrame(getcsv)

b=df["Avg Games til Next Win"]

print(b)

for each in b:
    print(f'something here {each} is {type(each)}')

print(type(df["Avg Games til Next Win"]))

# instead of df.key you can use the classic key method because the title has spaces in it.
# b=df["Avg Games til Next Win"].astype(int)

print(b)