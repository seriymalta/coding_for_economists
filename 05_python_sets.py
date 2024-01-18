#Intro to datat set

#Set is a collection of well defined objects
mySet = {1,2,3,4,5,6,7,8,9,10}

print(mySet)

#Check type
print(type(mySet))

mySet = {1,2,3,3}

print(mySet)

#Check membership
print(1 in mySet)

print(set('aaaaaaaabbbbbbbbbccccccccc'))

#Define two sets and check out set operation

setA = {1, 2, 3}
listB = [3, 4, 5, 5, 5 , 5 , 5 , 5 , 5 , 5 , 5]
setB =  set(listB)

print(setA, setB)

#Set Union
unionAB = setA | setB

print(unionAB)

#Intersection

intersecAB = setA & setB
print(intersecAB)

#Difference
diffAB = setA - setB
print(diffAB)