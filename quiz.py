import tkinter as tk
from tkinter import *

class QuizApplication:
    
    """The user will decide whether they want to
    iteratively input questions with each answer choice (A-D)
    if consoleInputQNA is set to True. Otherwise, the questions are
    read from a file."""
    def __init__(self, root=tk.Tk(), numQuestions=2, consoleInputQNA=True):
        self.root = root
        self.numQuestions = numQuestions
        # Dictionary containing questions and answer choices
        self.QNA = {}
        self.numCorrect = 0
        
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
            
    # Acutal quiz for user
    def takeQuiz(self):
        for question, answer in self.QNA.items():
            print(f"{question}:\nA. {answer[0]}\nB. {answer[1]}\nC. {answer[2]}\nD. {answer[3]}")
            userChoice = input("--> ")
            if userChoice==answer[-1]:
                print("CORRECTO!!!")
                
    
myQuiz = QuizApplication()
myQuiz.inputQNA()
myQuiz.takeQuiz()
