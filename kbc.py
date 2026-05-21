# This program is a simple implementation of the popular game "Kaun Banega Crorepati" (KBC) in Python. 
# The program presents a series of multiple-choice questions to the user, and the user must select the correct answer to win money. The user can win increasing amounts of money with each correct answer, but if they answer incorrectly, they lose the game. 
# The program also keeps track of the money won by the user and displays it at the end of the game.

# List of questions, options, and correct answers
Questions = [["Who is the founder of Microsoft?","A. Bill Gates","B.Steve Jobs","C.Mark zukerburg","D.Larry Page",1],
["Taj Mahal is located in which city?","A. Agra","B. Delhi","C. Jaipur","D. Mumbai",1],
["Tallest mountain in the world?","A. K2","B. Kangchenjunga","C. Mount Everest","D. Lhotse",3],
 ["which is the largest ocean in the world?","A. Atlantic Ocean","B. Indian Ocean","C. Arctic Ocean","D. Pacific Ocean",4],
 ["Who is the current president of USA?","A. Joe Biden","B. Donald Trump","C. Barack Obama","D. George Bush",2],
 ["Which is the largest country in the world?","A. China","B. Russia","C. USA","D. Canada",2],
["Which is the most selling manga in the world?","A. One Piece","B. Naruto","C. Dragon Ball","D. Detective Conan",1],
 ["Who is the mangakar of One Piece?","A. Masashi Kishimoto","B. Eiichiro Oda","C. Akira Toriyama","D. Gosho Aoyama",2],
 ["which is the most selling video game in the world?","A. Minecraft","B. Grand Theft Auto V","C. Tetris","D. Wii Sports",1],
 ["Which is the most used programming language in the world?","A. Python","B. JavaScript","C. Java","D. C++",1]]
# List of money levels for each question
Levels=[1000,3000,5000,10000,100000,150000,300000,500000,1000000,5000000]
print("Welcome to KBC")
# Initializing the money variable to keep track of the user's winnings
Money=0
# Looping through the questions and presenting them to the user
for i in range (0,len(Questions)):
    question=Questions[i]
    print(f"{question[0]}\n for rs {Levels[i]}")
    print(f"{question[1]}        {question[2]}")
    print(f"{question[3]}        {question[4]}")
    reply=int(input("Enter your answer(1-4) :"))

    if (reply==question[5]):
        print(f"Congratulations you have won rs{Levels[i]}!")
    # Updating the money variable based on the current level of the game
        if(i==4):
            Money=10000
        elif(i==9):
            Money=300000
    else:
        print("Sorry you have Lost the game")
        break 
    # Displaying the money won by the user at the end of the game
print(f"Money you will take home {Money}")
   

