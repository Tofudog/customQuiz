import tkinter as tk
from tkinter import *
from functools import partial
from time import sleep

class QuizApplication:
    
    """The user will decide whether they want to
    iteratively input questions with each answer choice (A-D)
    if consoleInputQNA is set to True. Otherwise, the questions are
    read from a file."""
    def __init__(self, root=tk.Tk(), numQuestions=3, consoleInputQNA=True):
        self.root = root
        self.numQuestions = numQuestions
        self.chosenLetter = None
        
        # Dictionary containing questions and answer choices
        self.QNA = {}
        self.numCorrect = 0
        self.currentQuestion = -1
        
        # GUI buttons and labels
        self.labelQuestion = tk.Label(root, text="")
        self.buttonA = tk.Button(root, bg="red", text="")
        self.buttonB = tk.Button(root, bg="red", text="")
        self.buttonC = tk.Button(root, bg="red", text="")
        self.buttonD = tk.Button(root, bg="red", text="")
        self.next = tk.Button(root, bg="pink", text="next", command=self.nextButton)
        self.back = tk.Button(root, bg="pink", text="back", command=self.backButton)
        self.confirmAnswer = tk.Button(root, bg="pink", text="select", command=self.confirm)
        
        # Placing buttons and labels
        self.labelQuestion.grid(row=0, column=1, padx=10, pady=100)
        self.buttonA.grid(row=1, column=1, padx=75, pady=25, ipadx=200, ipady=20)
        self.buttonB.grid(row=2, column=1, padx=75, pady=25, ipadx=200, ipady=20)
        self.buttonC.grid(row=3, column=1, padx=75, pady=25, ipadx=200, ipady=20)
        self.buttonD.grid(row=4, column=1, padx=75, pady=25, ipadx=200, ipady=20)
        self.next.grid(row=5, column=2, padx=500, pady=0, ipadx=30, ipady=10)
        self.back.grid(row=5, column=0, padx=10, pady=0, ipadx=30, ipady=10)
        self.confirmAnswer.grid(row=1, column=2, ipadx=30, ipady=10)
        
    # User-generated QNA if consoleInputQNA is True
    def inputQNA(self):
        for i in range(self.numQuestions):
            question = input(f"Type in Question #{i+1}: ")
            answerA = input(f"What is Answer choice A? ")
            answerB = input(f"What is Answer choice B? ")
            answerC = input(f"What is Answer choice C? ")
            answerD = input(f"What is Answer choice D? ")
            correctAnswer = input("What is the correct answer (A-D)? ")
            self.QNA[question] = [answerA, answerB, answerC, answerD, correctAnswer]
    
    # Alternative to test taker inputting QNA on console
    def readQNAFromFile(self, file):
        questions = []
        answers = []
        with open(file) as fr:
            for n, line in enumerate(fr.readlines()):
                # Line with question
                if n%6==0:
                    questions.append(line[2:-1])
                else:
                    answers.append(line[2:-1])
        
        # Updating len of numQuestions defined in init
        self.numQuestions = len(questions)
                    
        for n, question in enumerate(questions):
            self.QNA[question] = answers[0:5]
            del answers[0:5]  
    
    def answerUser(self, letter):
        self.chosenLetter = letter
        
    def nextButton(self):
        self.currentQuestion += 1
        self.answerQuestion()
        
    def backButton(self):
        self.currentQuestion -= 1
        self.answerQuestion()
        
    def confirm(self):
        if self.chosenLetter == self.answer1[-1]:
            self.numCorrect += 1
            print("Correct")
    
    # Acutal quiz for user
    def answerQuestion(self): 
        question, answer = self.QNA.keys(), self.QNA.values()
        self.question = list(question)[self.currentQuestion]
        self.answer = list(answer)[self.currentQuestion]
        
        self.labelQuestion.config(text=self.question)
        self.buttonA.config(text=self.answer[0], command=partial(self.answerUser, "A"))
        self.buttonB.config(text=self.answer[1], command=partial(self.answerUser, "B"))
        self.buttonC.config(text=self.answer[2], command=partial(self.answerUser, "C"))
        self.buttonD.config(text=self.answer[3], command=partial(self.answerUser, "D"))
    


# quiz = QuizApplication(consoleInputQNA=False)
# quiz.readQNAFromFile("QNA.py")
# # tk.mainloop()
# qna = quiz.QNA
# q, a = qna.keys(), qna.values()
# print(q)
# print(a)

newQuiz = QuizApplication(numQuestions=2)
newQuiz.inputQNA()
print(newQuiz.QNA)














