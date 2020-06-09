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
    letter=input("please enter letter from the word:  ");
    while(letter!='5'):
    
        chk=cheack_valid_input(letter,old_letters);
        #cheack_valid_input(letter_guessed,old_letters_gussed):
        print(chk)
        letter=input("please enter letter from the word:  ");


if __name__ == "__main__":
    main();
