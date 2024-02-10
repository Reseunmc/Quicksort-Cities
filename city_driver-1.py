__author__ = 'Re'

from city import City
from quicksort import *


#opens the file world cities and produces an empty list
file_name="world_cities.txt"
in_file =open(file_name,"r" )
list=[]

#for loop to strip and split the line into a list. Appends the objects to the empty list and indexes for the
#object parameters after the line is stripped and split
for line in in_file:
    s= line.strip()
    sp= s.split(",")
    list.append(City(sp[0],sp[1],sp[2],sp[3],sp[4], sp[5]))

#close file
in_file.close()

#opens the cities_out file. For loop to index from the 0th index to one before the last and writes
#the string onto the file
out_file=open("cities_out.txt","w")
for line in list[0:-1]:
    out_file.write(line.__str__() + "\n")

#writes the all but the last index and closes the file
out_file.write(list[-1].__str__())
out_file.close()

file_name="world_cities.txt"
in_file =open(file_name,"r" )

#compares the city names and returns true
def compare_alpha(city1,city2):
    return city1.name.lower() < city2.name.lower()

#compares the city population
def compare_population(city1,city2):
    return city1.population<=city2.population

#compares the latitudes
def compare_latitudes(city1,city2):
    return city1.latitude<=city2.latitude

#creates the files for each of the comparison lists
def create_files():
    file_name="world_cities.txt"
    in_file =open(file_name,"r" )
    list=[]

#for loop to strip and split the line into a list. Appends the objects to the empty list and indexes for the
#object parameters after the line is stripped and split
    for line in in_file:
        s= line.strip()
        sp= s.split(",")
        list.append(City(sp[0],sp[1],sp[2],sp[3],sp[4], sp[5]))


#applies quick sort to the list using the compare_alpha function to sort in
#alphabetical order
    quicksort(list,0,len(list)-1,compare_alpha)
    out_file=open("cities_alpha.txt","w")

#iterates through the list and writes the to the out file.
    for line in list[0:-1]:
        out_file.write(line.__str__() + "\n")

#qicksorts based on population.
    quicksort(list,0,len(list)-1,compare_population)
    out_file=open("cities_population.txt","w")

#iterates through the list and writes the to the out file.
    for line in list[0:-1]:
        out_file.write(line.__str__() + "\n")

#qicksorts based on latitude.
    quicksort(list,0,len(list)-1,compare_latitudes)
    out_file=open("cities_latitudes.txt","w")
    for line in list[0:-1]:
        out_file.write(line.__str__() + "\n")


#writes the all but the last index and closes the file
    out_file.write(list[-1].__str__())
    out_file.close()

create_files()