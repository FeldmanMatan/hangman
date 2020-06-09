def check_win(secret_word, old_letters_guessed):
    flag=True
    letter=0;
    while((flag) and (letter < len(secret_word))):
        if secret_word[letter] not in old_letters_guessed:
            flag= False
        letter+=1
    return flag
 
def show_hidden_word(secret_word, old_letters_guessed):
    """function that get the secret word and list of letters that already entered, 
       and print the correct letters in the word and '_' inn letters that have not yet been discover
            :secret_word: word to find :str
            :old_letters_gussed: list fo the letters that already entered:list
            rtype:null"""
    letter=0
    for letter in range(0,len(secret_word)):
        if secret_word[letter] not in old_letters_guessed:
           print('_',end=' ')
        else: 
            print(secret_word[letter],end=' ')
        letter+=1
    print("\n",old_letters_guessed);
    return secret_word;

def print_old_letter(old_letters_gussed):
    """bla bla bla"""
    old_letters_gussed.sort()
    k=0
    i=len(old_letters_gussed)
    print('X')
    while (i>0):
        print(old_letters_gussed[k],end='->')
        k+=1
        i-=1
    print("\n") 
    
def cheack_valid_input(letter_guessed,old_letters_gussed):
    """function that get letter from gussed and check it is valid'
       if it is valid return true, else return false
            :letter_guessed: letter ftom the user:str
            :return: print the leester in small if it is true, else return false
            rtype:bool
    """
    if ((len(letter_guessed)>1) or (not(letter_guessed.isalpha()))):
        print_old_letter(old_letters_gussed)
        return False;
    elif letter_guessed.lower() in old_letters_gussed:
         print_old_letter(old_letters_gussed)
         return False;
    else:
        if (letter_guessed>='A') and (letter_guessed<='Z'):                   # cahnge big to small letter
            print("Guess a lletter: ",letter_guessed.lower());
        else: print("Guess a lletter = ", letter_guessed);
        old_letters_gussed.append(letter_guessed.lower())
        return True;
   
def main():
    old_letters=list()
    word=input("please enter word : ");
    word=word.lower()
    print('_ '*len(word))
    #letter=input("please enter letter from the word:  ");
    
    for i in range(1,5):
      letter=input("please enter letter from the word:  ");
      chk=cheack_valid_input(letter,old_letters);
      show_hidden_word(word, old_letters)
    if(check_win(word, old_letters)):
        print("wiinner")
    else:
         print("looser")
     
        #cheack_valid_input(letter_guessed,old_letters_gussed):
 
if __name__ == "__main__":
    main();