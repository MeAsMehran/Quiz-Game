
import random

class Question:
    def __init__(self, text, wrongAsw1, wrongAsw2, wrongAsw3, correctAsw):
        self.text = text
        self.wrongAsw1 = wrongAsw1
        self.wrongAsw2 = wrongAsw2
        self.wrongAsw3 = wrongAsw3
        self.correctAsw = correctAsw
        self.showingChoices = self.showing_choices()


    def showing_choices(self):

        # this while works like do-while loop
        while True:
            choice1 = random.randint(0, 3)
            choice2 = random.randint(0, 3)
            choice3 = random.randint(0, 3)
            choice4 = random.randint(0, 3)
            if not self.not_reapetd(choice1, choice2, choice3, choice4):
                break

        choiceslist = []
        choiceslist.insert(choice1, self.wrongAsw1)
        choiceslist.insert(choice2, self.wrongAsw2)
        choiceslist.insert(choice3, self.wrongAsw3)
        choiceslist.insert(choice4, self.correctAsw)
        # choiceslist[choice1] = self.wrongAsw1
        # choiceslist[choice2] = self.wrongAsw2
        # choiceslist[choice3] = self.wrongAsw3
        # choiceslist[choice4] = self.correctAsw

        return choiceslist



    def __str__(self):
        return self.text



    def checking_answer(self, choice:int) -> bool:
        # dictionaryAns = {'correct': self.correctAsw, 'wrong1': self.wrongAsw1, 'wrong2': self.wrongasw2, 'wrong3': self.wrongasw3}
        if self.showingChoices[int] is self.correctAsw:
            return True        # win
        else:
            return False       # lose




    def not_reapetd(self, choice1, choice2, choice3, choice4):
        choiceslist = list((choice1, choice2, choice3, choice4))
        for i in range(len(choiceslist) - 1):
            for j in range(i + 1, len(choiceslist)):
                if choiceslist[i] == choiceslist[j]:
                    return False    # choices number as index are not different from each other
                else:
                    continue

        return True     # choices number as index are different from each other