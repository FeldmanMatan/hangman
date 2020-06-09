def start_screen():

    """function that print the start screen
            rtype:null """

    HANGMAN_ASCII_ART=("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""");

    print(HANGMAN_ASCII_ART);
    print("\nWellcome to HANGMAN game :)");

def choose_word(file_path, index):    #5
    """function that get file path of txt file and index(number greater zero) from gussed
        and return word.
            :file_path: path of file txt :str
            :index: number greater zero to choose word for the game: int
            :return: word from the file
            rtype:str"""

    with open(file_path, "r")  as file_open:                                         #open the file
        cd_data = file_open.read();                                                   #read the Reads the contents of the file into  cd_data
        cd_splitted_word = cd_data.split(" ");                                        #Separates the text into single words
        length=len(cd_splitted_word);
        num_word=(int(index) % length-1);                                            #return the number of word that we choose
        return(cd_splitted_word[num_word]);



def print_hangman(num_of_tries):
    """function that get num_of_tries, and print HANGMAN photo.
            :num_of_tries :int
            rtype:null"""
    
    print(HANGMAN_PHOTHO[num_of_tries]);
    #print("\n\nYou have another %d  attempts left out of %d\n" % ((MAX_TRIES-num_of_tries), MAX_TRIES));  #    option to add

def try_update_letter_guessed(letter_guessed,old_letters_gussed): #4
    """function that get letter from gussed and check it is valid'
       if it is valid return true, else return false
            :letter_guessed: letter ftom the user:str
            :old_letters_gussed: list fo the letters that already entered:list
            :return: true the letter valid and not yet inserted, else return false and the letter guessed
            rtype:bool,str"""
   
    if ((letter_guessed >= 'A') and (letter_guessed <= 'Z')):            #Checks if a Capital letter is inserted
         letter_guessed=letter_guessed.lower();                      #.. And changes it to a small letter
    check=check_valid_input(letter_guessed, old_letters_gussed) ;      #send to function to check if is is valid letter 
    if (check == False):
        old_letters_gussed.sort();
        print('X');
        for i in range(0, (len (old_letters_gussed))):
            print(old_letters_gussed[i], end = '->');
        print("\n");
        return False, letter_guessed;

    else:
            old_letters_gussed.append(letter_guessed);
            return True, letter_guessed;

    
def cheack_valid_input(letter_guessed, old_letters_gussed):    #3
    """function that get letter  it is valid'
       if it is valid return true, else return false
            :letter_guessed: letter ftom the user:str
            :old_letters_gussed: list fo the letters that already entered:list
            :return: true the letter valid , else return false
            rtype:bool
    """
    if ((len (letter_guessed) > 1) or (not (letter_guessed.isalpha()))):     #cheack if the input is valid
        return False;
    elif (letter_guessed.lower() in old_letters_gussed):                   #Checks if the letter already exists in the list
         return False;
    else:
        return True;


 
def show_hidden_word(secret_word, old_letters_guessed): #2
    """function that get the secret word and list of letters that already entered, 
       and print the correct letters in the word and '_' inn letters that have not yet been discover
            :secret_word: word to find :str
            :old_letters_gussed: list fo the letters that already entered:list
            rtype:null"""

    letter = 0;
    for letter in range(0, len(secret_word)): 
        if secret_word[letter] not in old_letters_guessed:  
           print('_', end=' ');
        else: 
            print(secret_word[letter], end=' ');
        letter+= 1;
    print("\n");
   
   
def check_win(secret_word, old_letters_guessed):    #1

    """function that get the secret word and list of letters that already entered, 
       and check if all the letters in the word were detected and player won
            :secret_word: word to find :str
            :old_letters_gussed: list fo the letters that already entered:list
            :return: if all the letters in the word were detected return true, else false 
            rtype:bool """

    flag= True;
    letter= 0;
    while((flag) and (letter < len(secret_word))):
        if secret_word[letter] not in old_letters_guessed:
            flag= False;
        letter+= 1;
    return flag;

MAX_TRIES= 6;
HANGMAN_PHOTHO= {
    1: """
    x-------x
    """,
    2: """
    x-------x
    |
    |
    |
    |
    |
    """,
    3:"""
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7:"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """  }

def main():

    flag_of_win= False;
    num_of_tries = 1; 
    old_letters_guessed= list();

    start_screen();                                                                      # print the start scree
    file_path = input("please enter path of txt file: ");
    index = input("please enter number Greater than zero of word from the txt file: ");
    secret_word = choose_word(file_path, index);                                          # find the secret word from the file
    print("\nlets start !!! Good luck :)\n");
    print_hangman(num_of_tries);                                                         # print the Hangman
    while((num_of_tries <= MAX_TRIES) and (flag_of_win == False)): 
       
        show_hidden_word(secret_word, old_letters_guessed);                              # print the hidden word
        letter_guessed= input("\nplease enter letter from the word:  ");
        chk, letter_guessed=try_update_letter_guessed(letter_guessed,  old_letters_guessed);             # check if the input is valid and if it is not exist.
        if (chk == False):                                                               # if it is invalid or exist
            num_of_tries+= 1;
            print("wrong answer...  :(   ");
            print_hangman(num_of_tries);
        elif (letter_guessed  not in secret_word):                                       # if it is valid but wrong letter  
              num_of_tries+= 1;
              print_hangman(num_of_tries);
        else:
            flag_of_win = check_win(secret_word, old_letters_guessed);                    # check if win

    if (flag_of_win):
        show_hidden_word(secret_word, old_letters_guessed);
        print("\nCongratulations, you have been able to identify the hidden word :) ");
        
    else:
        print("\n\nYou lost, try again later :( ");

   
if __name__ == "__main__":
    main();
