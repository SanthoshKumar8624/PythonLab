"""
Question: Implementing Programs using written modulus and python Standerd Libraries (pandas)
"""

import pandas as pd

data = {
    "Names": ["Jai", "Princi", "Gaurav", "Arun"],
    "Age": [21, 22, 23, 24],
    "Address": ["USA", "UK", "UAE", "India"],
    "Qualificaion": ["MCA", "MBA", "MA","Phd"]
}

df = pd.DataFrame(data)
print(df)


"""
OUTPUT:
-----

    Names  Age  Address  Qualificaion
0     Jai   21      USA           MCA
1  Princi   22       UK           MBA
2  Gaurav   23      UAE            MA
3    Arun   24    India           Phd

"""