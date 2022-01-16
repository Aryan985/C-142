import csv

allmovies = []
headers = []
with open("finalMovies.csv",encoding="utf8")as f:
    read = csv.reader(f)
    df = list(read)
    allmovies = df[1:]
    headers=df[0]

headers.append("poster")
with open("final.csv","a+",encoding="utf8")as a:
    write = csv.writer(a)
    write.writerow(headers)

with open("movie_links.csv",encoding="utf8")as f:
    read = csv.reader(f)
    df = list(read)
    allmovieslink = df[1:]

for i in allmovies:
    posterfound = any(i[8] in j for j in allmovieslink) 
    if posterfound:
        for m in allmovieslink:
            if i[8]==m[0]:
                i.append(m[1])
                with open("final.csv","a+",encoding="utf8")as a:
                    write = csv.writer(a)
                    write.writerow(i)