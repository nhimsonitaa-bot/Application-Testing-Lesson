import pandas as pd

df = pd.DataFrame(
    [["Raphael", "red", "sai"], 
     ["Donatello", "purple", "bo staff"]],
    columns=["name", "mask", "weapon"],
)

df.to_csv("out.csv", index=False)

print(df)