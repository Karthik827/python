sentence = input("enter a word")
string = sentence.lower()
list1 = ["a","e","i","o","u"]
count = 0
for char in list1:
    if char in list1:
        count = count+1

print("number of vowels are",count)