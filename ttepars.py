import pandas as pd
from datab import Original
from prime import *

a = pd.read_csv("NetflixOriginals.csv", encoding="ISO-8859-1")
print(a)
sl = {}
current = 2
for row in a.values:
    a = row[1]
    b = a.split("/")
    for you in b:
        if you in sl.keys():
            pass
        else:
            sl[you] = current
            current = prime(current)
    p = 1
    for name in b:
        p = p * sl[name]
    Original.create(Title = row[0], Genre = p, Premiere = row[2], Runtime = row[3],
                     IMDB_Score = row[4], Language = row[5])
print(sl)

# for row in a.values:
    
#     Original.create(Title = row[0], Genre = , Premiere = row[2], Runtime = row[3],
#                      IMDB_Score = row[4], Language = row[5])


