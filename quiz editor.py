import json

def dump_questions():
    with open("questions.json", "w") as f:
        json.dump(questions, f)
        
def load_questions():
    with open("questions.json", "r") as f:
        return json.load(f)
    
def dump_highscore():
    with open("highscore.json", "w") as f:
        json.dump(highscore, f)

def load_highscore():
    try:
        with open("highscore.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"highscore": 0}

questions = load_questions()
while True:
    load_highscore()
    start = input("Would you like to edit the quiz, (y/n): ")
    
    if start.lower() == "y":
        print("1. Add a question")
        print("2. Delete a question")
        print("3. Change a question")
        
        del_or_change = input("Choose: ")
        if del_or_change == "1":
            newquestion = input("What is the new question: ")
            newanswer = input("what is the anwser to this question: ")
            question = {"question": newquestion, "answer": newanswer}
            questions.append(question)  
            dump_questions()
            highscore = 0
            dump_highscore()
            
        elif del_or_change == "2":
            for i, q in enumerate(questions, 1):
                print(i, q["question"])
            try:
                delete = int(input("Delete? or [s]top: "))
                if delete == "s":
                    continue
                delq = delete - 1
                if 0 <= delq < len(questions):
                    questions.pop(delq)
                    dump_questions()
                    highscore = {"highscore": 0}
                    dump_highscore()
                    print("Deleted!")
                else:
                    print("Invalid number!")
            except ValueError:
                print("\n")
        
        elif del_or_change == "3":
            for i, q in enumerate(questions, 1):
                print(i, q["question"], "\tanswer: ", q["answer"])
            change = int(input("Which to change: "))
            change -= 1
            print(questions[change])
            answ_or_quest = input("Answer or question: ")
            if answ_or_quest.lower() == "a":
                if answ_or_quest.lower() == "a":
                    edanswer = input("New answer: ")
                    questions[change]["answer"] = edanswer
                    dump_questions()
                    print("Answer updated!")
                elif answ_or_quest.lower() == "q":
                    edquestion = input("New question: ")
                    questions[change]["question"] = edquestion
                    dump_questions()
                    print("Question updated!")
                
                             
    elif start.lower() == "n":
        break
    else:
        print("val error")


