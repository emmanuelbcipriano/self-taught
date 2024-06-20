import csv

movie_table = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

#write to a csv file
with open('movies.csv','w') as f:
    w = csv.writer(f, delimiter=',')
    for movie_row in movie_table:
        w.writerow(movie_row)

#print to console
with open('movies.csv','r') as f:
    r = csv.reader(f,delimiter=',')
    for row in r:
        print(','.join(row))