class QuizBrain:
    def __init__(self, questions):
        self.question_num = 0
        self.questions = questions
        self.score = 0
        self.game_over = False

    def start_game(self):
        answer = input("Are you ready to play? (Y/N) :")
        if answer == "Y":
            print("Let's start!")
            print("**** Type 'quit' at anytime to exit the game ****")
            print("--------------------------------------")
            self.next_question()
        else:
            print("Goodbye!")

    def next_question(self):
        while self.question_num < len(self.questions) and not self.game_over:
            answer = input("Q." + str(self.question_num + 1) + ": " + self.questions[self.question_num].text + " (True/False)?: ")
            if answer.lower() == self.questions[self.question_num].answer.lower():
                print("Correct!")
                self.score += 1
            elif answer.lower() == "quit":
                self.game_over = True
                break
            else:
                print("Boo, WRONG. The answer is {}".format(self.questions[self.question_num].answer))
            self.question_num += 1
            print("--------------------------------------")
        self.print_score()

    def print_score(self):
        print("Your score is {}/{}.".format(self.score, len(self.questions)))
        print("Thanks for playing!!")
