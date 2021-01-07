class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        self.check_answer(input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} "
                                f"(True/False): "),self.questions_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("This answer is correct!")
            self.score += 1
        else:
            print("Sorry, wrong answer.")
        if self.question_number < len(self.questions_list) - 1:
            print(f"Your current score is {self.score}/{self.question_number + 1}\n")
        else:
            print(f"Your final score is {self.score}/{self.question_number + 1}\n")
