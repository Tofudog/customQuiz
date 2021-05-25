# customQuiz
An application that allows a user to create their own quiz and receive feedback on missed questions.

# How does the quiz application work?
The test-taker has two options: either to manually type in the questions, answer choices, and the answers (for the sake of concision, we will refer to this dictionary as QNA) via the command line or type in the QNA in a separate file (text, .py, etc.) and have the computer read it. Personally, I would prefer the latter- having to type in 10 QNA’s with the risk of messing up is not fun- but there are both options. Once the test-taker clicks the “next” button, the quiz will begin! Each question will contain four buttons representing answer choices (A-D). The test-taker can click on as many choices as they want but only “score” the response once (using a separate button), where the program will evaluate if the response is “correct” (yielding a point) or “incorrect”. The process repeats while self.currentQuestion < self.numQuestions. 


Still to be finished: the bar chart modelling correct/incorrect questions.
