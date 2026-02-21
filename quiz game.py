import json

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
        
question_count = 0
wrong_count = 0
cor_count = 0
highscore = load_highscore()
best_score = highscore["highscore"]


questions = load_questions()

print("Welcome to the quiz.")
start_or = input("[s]tart the quiz or see your [h]ighscore or [q]uit: ")
while True:
    if start_or.lower() == "s":
        while True:
            for q in questions:
                question_count += 1
                answer = input(q["question"] + " ")
                
                if answer.lower() == q["answer"]:
                    cor_count += 1
                    print("Correct!")
                else:
                    print(f"Wrong! The answer was {q['answer']}.")
                    wrong_count += 1
                    
            print("\nYou finished the quiz with a score: ", cor_count, "/", question_count)
            
            if cor_count > best_score:
                print("This is your new high score!")
                highscore["highscore"] = cor_count
                dump_highscore()
                
            question_count = 0
            wrong_count = 0
            cor_count = 0
            again = input("Try again (y/n): ")
            if again == "n":
                break
                
    elif start_or.lower() == "h":
        print("Your best score is: ", best_score, "/", len(questions))
    elif start_or.lower() == "q":
        exit()
    
    start_or = input("\n[s]tart the quiz or see your [h]ighscore or [q]uit: ")

            
    

    







