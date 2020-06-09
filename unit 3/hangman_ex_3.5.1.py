#letter=input("please enter letter from the word:   ");
#if (letter>='a') and (letter<='z'):
#    print("Guess a lletter = ", letter); 
#elif (letter>='A') and (letter<='Z'):
#    print("small letter: ",letter.lower());
#else :
#    print("leeter=", letter)
word=input("please enter word : ");
print('_ '*len(word))

letter=input("please enter letter from the word:  ");
if (letter>='a') and (letter<='z'):
    print("Guess a lletter = ", letter);
elif (letter>='A') and (letter<='Z'):
   print("Guess a lletter: ",letter.lower());
elif((len(letter)>1) and (isalpha(letter))):
     print("E!1")
