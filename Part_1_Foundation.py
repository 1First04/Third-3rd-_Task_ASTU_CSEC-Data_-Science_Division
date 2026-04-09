import pandas as pd
presidents = {
    "P31": ["Herbert Hoover", "Iowa", "Republican", 1929, 1874],
    "P32": ["Franklin D. Roosevelt", "New York", "Democratic", 1933, 1882],
    "P33": ["Harry S. Truman", "Missouri", "Democratic", 1945, 1884],
    "P34": ["Dwight D. Eisenhower", "Texas", "Republican", 1953, 1890],
    "P35": ["John F. Kennedy", "Massachusetts", "Democratic", 1961, 1917],
    "P36": ["Lyndon B. Johnson", "Texas", "Democratic", 1963, 1908],
    "P37": ["Richard Nixon", "California", "Republican", 1969, 1913],
    "P38": ["Gerald Ford", "Nebraska", "Republican", 1974, 1913],
    "P39": ["Jimmy Carter", "Georgia", "Democratic", 1977, 1924],
    "P40": ["Ronald Reagan", "Illinois", "Republican", 1981, 1911],
    "P41": ["George H. W. Bush", "Massachusetts", "Republican", 1989, 1924],
    "P42": ["Bill Clinton", "Arkansas", "Democratic", 1993, 1946],
    "P43": ["George W. Bush", "Connecticut", "Republican", 2001, 1946],
    "P44": ["Barack Obama", "Hawaii", "Democratic", 2009, 1961],
    "P45": ["Donald Trump", "New York", "Republican", 2017, 1946]
}
columns = ["Name", "State", "Party", "Term_Start", "Birth_Year"]

df = pd.DataFrame.from_dict(presidents, orient="index", columns=columns) # from_dict() = convert dictionary → DataFrame, orient="index" = keys become rows

print(df)
