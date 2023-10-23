myList = ["oranges","apples","bananas", "pineapple"]
myList2 = ["oranges","apples","bananas", "pineapple",[1, 1, 2, 3, 5, 8, 13, 21, 34],"hello world python"]
print(myList)
print(myList2)
print(len(myList2))  #size of the list
myList.append(["The list of fruits i like"]) #adding an element to the list
print(myList)

#output
# ['oranges', 'apples', 'bananas', 'pineapple']
# ['oranges', 'apples', 'bananas', 'pineapple', [1, 1, 2, 3, 5, 8, 13, 21, 34], 'hello world python']
# 6
# ['oranges', 'apples', 'bananas', 'pineapple', ['The list of fruits i like']]


#Conversion of a string into a list using split() function

message = "I love fruits so much"
print(message.split())

#output
#['I', 'love', 'fruits', 'so', 'much']