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
if ((len(letter)==1) and (letter.isalpha())):             # small letter in alpha-beta
    if (letter>='A') and (letter<='Z'):                   # cahnge big to small letter
        print("Guess a lletter: ",letter.lower());
    else: print("Guess a lletter = ", letter);

elif((len(letter)>1) and (letter.isalpha())):          # string in alpha-beta 
     print("E1")
elif((len(letter)>1) and (not(letter.isalpha()))):     # string with not only alpha-beta
     print("E3");
elif((len(letter)==1) and (not(letter.isalpha()))):    # not alpha-beta letter
     print("E2");