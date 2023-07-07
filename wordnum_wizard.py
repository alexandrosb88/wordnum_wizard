#wordnum_wizard

# Copyright (c) 2023 alexandrosb88

def plain_numbers_1_to_999(word):
    list_n = []
    for i in range(1000):
        list_n.append(word + str(i) + "\n")

    for i in range(10):
        list_n.append(word + "0" + str(i) + "\n")
        list_n.append(word + "0" + str(i) +"0" + str(i) + "\n")

    for i in range(100):
        list_n.append(word + str(i) + str(i) + "\n")
        

    return list_n

def year(word):
    list_n = []
    for i in range(1900,2023):
        list_n.append(word + str(i) + "\n")

    list_n.append(word + "1821" + "\n")
    
    return list_n

def dates(word):
    list_n = []
    for i in range(1,32):
        for j in range(1,13):
            if j > 10 and i > 10:
                list_n.append(word + str(i) + str(j) + "\n")
            elif j < 10 and i < 10:
                list_n.append(word + "0" + str(i) + "0" + str(j) + "\n")
            elif j > 10 and i < 10:
                list_n.append(word + "0" + str(i) + str(j) + "\n")
            elif j < 10 and i > 10:
                list_n.append(word + str(i) + "0" + str(j) + "\n")

    return list_n

def dates_plus_year(word):
    list_n = []
    for i in range(1,32):
        for j in range(1,13):
            for k in range(1960,2023):
                if j > 10 and i > 10:
                    list_n.append(word + str(i) + str(j) + str(k) + "\n")
                elif j < 10 and i < 10:
                    list_n.append(word + "0" + str(i) + "0" + str(j) + str(k) + "\n")
                elif j > 10 and i < 10:
                    list_n.append(word + "0" + str(i) + str(j) + str(k) + "\n")
                elif j < 10 and i > 10:
                    list_n.append(word + str(i) + "0" + str(j) + str(k) + "\n")

    return list_n

def dates_plus_year2(word):
    list_n = []
    for i in range(1,32):
        for j in range(1,13):
            for k in range(10,61):
                if j > 10 and i > 10:
                    list_n.append(word + str(i) + str(j) + str(k) + "\n")
                elif j < 10 and i < 10:
                    list_n.append(word + "0" + str(i) + "0" + str(j) + str(k) + "\n")
                elif j > 10 and i < 10:
                    list_n.append(word + "0" + str(i) + str(j) + str(k) + "\n")
                elif j < 10 and i > 10:
                    list_n.append(word + str(i) + "0" + str(j) + str(k) + "\n")

    for i in range(1,32):
        for j in range(1,13):
            for k in range(1,10):
                if j > 10 and i > 10:
                    list_n.append(word + str(i) + str(j) + "0" + str(k) + "\n")
                elif j < 10 and i < 10:
                    list_n.append(word + "0" + str(i) + "0" + str(j) + "0" + str(k) + "\n")
                elif j > 10 and i < 10:
                    list_n.append(word + "0" + str(i) + str(j) + "0" + str(k) + "\n")
                elif j < 10 and i > 10:
                    list_n.append(word + str(i) + "0" + str(j) + "0" + str(k) + "\n")

    return list_n

def symbols_plus_numbers(word):
    list_n = []
    for i in range(100):
        list_n.append(word + "_" + str(i) + "\n")
        list_n.append(word + "-" + str(i) + "\n")
        list_n.append(word + "." + str(i) + "\n")

    for i in range(10):
        list_n.append(word + "_" + "0" + str(i) + "\n")
        list_n.append(word + "-" + "0" + str(i) + "\n")
        list_n.append(word + "." + "0" + str(i) + "\n")

    for i in range(1900,2023):
        list_n.append(word + "_" + str(i) + "\n")
        list_n.append(word + "-" + str(i) + "\n")
        list_n.append(word + "." + str(i) + "\n")

    return list_n


option = 0        

while option !=1 or option !=2:

    option = input(str('''Would you like to import a wordlist or manually provide the desired word(s)? (type 1 or 2): '''))

    if option == "1":

        #Input and output files 
        inputFile = input("Please specify the path of the txt file to be processed: ")
        outputFile = input("Please specify the name of the output file: ")

        #Read file
        file = open(inputFile)

        #Move words to list
        wordlist = []
        for word in file.read().split("\n"):
            wordlist.append(word)


        new_wordlist = []

        for n in wordlist:
            n = plain_numbers_1_to_999(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in wordlist:
            n= year(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in wordlist:
            n = dates(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in wordlist:
            n = dates_plus_year(n)
            n = ''.join(n)

            new_wordlist.append(n)
        
        for n in wordlist:
            n = dates_plus_year2(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in wordlist:
            n = symbols_plus_numbers(n)
            n = ''.join(n)

            new_wordlist.append(n)
        

        new_wordlist_string =''.join(new_wordlist)
        new_wordlist_string ='\n'.join(new_wordlist)

        #Export file
        file = open(outputFile + ".txt", "w")
        file.write(new_wordlist_string)
        file.close()
        print("File Created!")

    elif option == "2":

        cont = "Y"
        keywords = []
        while cont == "Y":
            word = input("Please specify the desired word: ")
            keywords.append(word)
            cont = (input("Would you like to add another word? (Y - N)")).upper()


        new_wordlist = []

        outputFile = input("Please specify the name of the output file: ")

        for n in keywords:
            n = plain_numbers_1_to_999(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in keywords:
            n= year(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in keywords:
            n = dates(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in keywords:
            n = dates_plus_year(n)
            n = ''.join(n)

            new_wordlist.append(n)

        for n in keywords:
            n = symbols_plus_numbers(n)
            n = ''.join(n)

            new_wordlist.append(n)

        new_wordlist_string =''.join(new_wordlist)
        new_wordlist_string ='\n'.join(new_wordlist)

        #Εxport file
        file = open(outputFile + ".txt", "w")
        file.write(new_wordlist_string)
        file.close()
        print("File Created!")

    else:
        print("\n")
        print("Please enter a valid option.")
        print("\n")
        




