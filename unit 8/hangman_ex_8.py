HANGMAN_PHOTHO={1: """
    x-------x
    """,2: """
    x-------x
    |
    |
    |
    |
    |
    """,3:"""
    x-------x
    |       |
    |       0
    |
    |
    |
    """,4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,7:"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """  }

def print_hangman(num_of_tries):
    """bla bla bla"""
    print(HANGMAN_PHOTHO[num_of_tries])

def main():
    
    for i in range(1,8):
        print_hangman(i)

if __name__ == "__main__":
    main();

   