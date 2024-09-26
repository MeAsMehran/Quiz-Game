
import Question
import random as ran


question = Question.Question("sdfasfasfa", 1, 2, 3, 4)
print(question)


class QuestionsSource:

    questions:Question = []      # creating a list for questions
    questionsForm:Question = []

    def addQusetion(self, question:Question):
        self.questions.append(question)




    def deleteQuestion(self, question:Question):
        self.questions.remove(question)



    def choosingQuestions(self):
        for _ in range(10):
            questionForm = ran.choice(self.questions)

        return questionForm



    # def choosingQuestions(self) -> list(Question):
    #     for _ in range(10):
    #         questionForm = ran.choice(self.questions)
    #
    #     return questionForm






