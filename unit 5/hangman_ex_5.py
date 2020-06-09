
def is_valid_input(letter_guessed):
    """function that get letter from gussed and check it is valid'
       if it is valid return true, else return false
            :letter_guessed: letter ftom the user:str
            :return: print the leester in small if it is true, else return false
            rtype:bool
    """
    if ((len(letter_guessed)>1) or (not(letter_guessed.isalpha()))):
        return False;
    else:
        if (letter_guessed>='A') and (letter_guessed<='Z'):                   # cahnge big to small letter
            print("Guess a lletter: ",letter_guessed.lower());
        else: print("Guess a lletter = ", letter_guessed);
        return True;
   
def main():
    letter=input("please enter letter from the word:  ");
    chk=is_valid_input(letter);
    print(chk)


if __name__ == "__main__":
    main();