#Character occurance
word = input("Enter word: ")
char = input("Enter character : ")
i = 0
count = 0
while(i < len(word)):
    if(word[i] == char): 
        count = count + 1
    i = i + 1

print("Above character has occured:" , count, "times")
