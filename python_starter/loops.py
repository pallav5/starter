# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).



# While loops execute a set of statements as long as a condition is true.

l1 = [1,2,3]
l2 = ['a','b','c']
l3 = []


for index,item in enumerate(l1):
    
    l3.append([item,l2[index]])

print(l3)   
    

list4 = [{'name':'ram'},{'name':'shyam'},{'name':'hari'},{'name':'ram'},{'name':'shyam'}]
# to print repeatead name only once

list5 =[]

for count in list4.values():
    if count  in list5:
        list5.append(count)
print(list5)   






    