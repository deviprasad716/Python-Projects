questions={
    1:{
        "question":"What is the capital of Australia?",
        "options":["Sydney","Melbourne","Canberra","Perth"],
        "answer":"Canberra"
    },
    2:{
        "question":"Which planet is known as the Red Planet?",
        "options":["Venus","Mars","Jupiter","Mercury"],
        "answer":"Mars"
    },
    3:{
        "question":"Who wrote the play Romeo and Juliet?",
        "options":["William Shakespeare","Charles Dickens","Mark Twain","George Orwell"],
        "answer":"William Shakespeare"
    }
}

def display_questions(question):
    print(question["question"])
    for index,option in enumerate(question['options']):
        print(index+1,option)

def ask_question(question):
    display_questions(question)
    user_choice=int(input("Enter your answer choice: "))
    user_choice-=1
    if question["answer"]==question["options"][user_choice]:
        print("Correct Answer!!")
        return True
    else:
        print("Wrong Answer!")
        return False

def run_quiz():
    score=0
    for key,value in questions.items():
        if ask_question(value):
            score+=1
    print("Your Score: ",score,"/",len(questions))

    with open("results.txt","w") as results_file:
        results_file.write(f"Quiz Result\nScore: {score}/{len(questions)}")

def show_result():
    with open("results.txt","r") as results_file:
        result=results_file.read()
        print(result)

def main():
    while True:
        print("===== QUIZ APPLICATION =====")
        print("1. Start Quiz.")
        print("2. Show previous result.")
        print("3. Exit.")

        choice=int(input("Enter choice: "))

        while not(0<choice<4):
            print("Invalid Choice..")
            print("===== QUIZ APPLICATION =====")
            print("1. Start Quiz.")
            print("2. Show previous result.")
            print("3. Exit.")
            choice=int(input("Enter your choice again: "))
        if choice==1:
            run_quiz()
        elif choice==2:
            show_result()
        elif choice==3:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()