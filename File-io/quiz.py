def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit the game")

    option =input("Enter option: ")
    return option
    
def ask_questions():
    questions = []
    answers = []
                                # we use the with block. It is self closing
    with open("quiz.txt", "r")as file: #read the file and split the lines
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines): #The enumerate function turns each of these lists to a tuple with a line number stored in i
        if i%2 == 0: #and the text is stored in text. 
            questions.append(text) #If I is even -line nmbr is even -then we know thats the question
        else:
            answers.append(text)
   
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)
    
    score = 0
            
    for question, answer in zip(questions, answers): #use zip function to put them together
        guess = input(question + "> ") #Här gör vi en input med vår gissning
        if guess == answer:
            score += 1
            print ("right")
            print(score)
        else:
            print("wrong")
    print("You got {0} correct out of {1}".format(score, number_of_questions))
            
def add_question():
    print("") #a space to make it look nice
    question = input("Enter a question\n> ") # use> as a prompt
    
    print("") #blankrad
    print("Ok then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    file = open("quiz.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def game_loop():
    while True: #just a way to say loop forewer (until exit)
        option = show_menu()
        if option =="1":
            ask_questions()
        elif option =="2":
            add_question()
        elif option == "3":
            break #med ordet break avslutar man spelet (break out of the loop)
        else:
            print("invalid option") #vanliga garderingen for ngn som skriver fel sak
    print("") #en blankrad för att fa det att se snyggare ut
    
game_loop()