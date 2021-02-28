
import csv

#data = csv.reader(data)  
#print(data)
with open(r"C:\Users\DHEERESH\Desktop\calculator\temp_saturated_water.csv", newline='') as csvfile:
    merifile = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in merifile:
        print(' '.join(row))
#data = open(r"C:\Users\DHEERESH\Desktop\calculator\temp_saturated_water.csv")
#data = csv.reader(data)
#print(data)
print()


