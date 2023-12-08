import csv

with open('sample.csv', 'r') as file:
   reader = csv.reader(file)
   data_list = list(reader)
    
print(data_list)