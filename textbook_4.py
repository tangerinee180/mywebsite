import numpy as np
import pandas as pd

df = pd.DataFrame({'name' : ["김지훈","이유진","박동현","김민지"],'english' : [90,80,60,70],
'math' : [50,60,100,20]})

df

type(df)

df["name"]
float(sum(df["english"])/len(df["english"]))

df2 = pd.DataFrame({"제품" : ["사과","딸기","수박"],
"가격" : [1800,1500,3000],
"판매량" : [24,38,13]
})

type(df2)
type(df2[["가격"]])
type(df2["가격"])


price_mean = sum(df2["가격"])/len(df2["가격"])
sold_mean = sum(df2["판매량"])/len(df2["판매량"])
