import pandas as pd

df = pd.DataFrame(
    [["Raphael", "red"], ["Donatello", "purple"]],
    columns=["name", "mask"],
)

print(df)

df.to_csv("out2.csv", index=False)

print(df)