def choose_word(file_path, index):
    """bla bla bla"""

    f = open(file_path, "r")
    cd_data = f.read()
    cd_splitted_word = cd_data.split(" ")
    #cd_splitted_word.sort()
    length=len(cd_splitted_word)
    print(cd_splitted_word,"  ",length)
    file_splited_word=[]
    len_word=0
    for i in range(0, length):
        if ((file_splited_word.count(cd_splitted_word[i]))==0):
            file_splited_word.append(cd_splitted_word[i])
            len_word+=1
    print(file_splited_word,"  ",len_word)
    print("length= ",len_word)
    num_word=(int(index)%length)
    print((int(index)%length))
    #print("word= ",cd_splitted_word[num_word])
    return(len_word,(cd_splitted_word[num_word]))
  
   # print("num word= ",len(cd_splitted_word))
    f.close()
    return()

def main():
    #file_path= r"C:\python\hangman\unit 9\exemple.txt"
    #index=3
    word=''
    file_path=input("please enter path of txt file: ")
    index=input("please enter number of word from the txt file: ")
    (length,word)=choose_word(file_path, index)
    print("word= ",word)
    print("length= ",length)
   


if __name__ == "__main__":
    main();

   

    
    
    
    