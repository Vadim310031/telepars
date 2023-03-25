import pandas as pd
from datab import Original


a = pd.read_csv("NetflixOriginals.csv", encoding="ISO-8859-1")
print(a)

for row in a.values:
    Original.create(Title = row[0], Genre = row[1], Premiere = row[2], Runtime = row[3],
                     IMDB_Score = row[4], Language = row[5])

