typein_string=input("Enter sentence or a word:")

print("\nManipulation options")
print("1.Change to lowercase")
print("2.Change to uppercase")
print("3.Slice the sentence")
print("4.Calculate expression length")
print ("5.Loop through characters")
print("6.Check hidden words")
print("7.Reverse your choosen word/sentence")

choice=int(input("Pick one option (1-7):"))

if choice ==1:
    result = typein_string.lower()
    print("Lowercase",result)

elif choice ==2:
    result= typein_string.upper()
    print("Uppercase:",result)
elif choice==3:
    start=int(input("Enter start index:"))
    end=int(input("Enter end index:"))
    result=typein_string[start:end]
    print("Sliced result :", result)
elif choice == 4:
    length=(len(typein_string))
    print("String length" ,length)
elif choice==5:
    print("Characters:")
    for char in typein_string:
        print(char)
elif choice ==6:
        word=input("Enter a letter or word to search:")
        sentence=typein_string
        
        if word in sentence:
            print("Match found:", word)
        else:
            print("No match found!")
elif choice==7:
    result=typein_string[::-1]
    print(result)
else: 
    print("Wrong choice")