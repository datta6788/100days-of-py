class QuizBrain:
    def __init__(self,que_list):
        self.que_num=0
        self.ql=que_list

    def questions_left(self):
        if self.que_num<len(self.ql):
            return True
        else:
            return False

    def questions(self):
        question=self.ql[self.que_num]
        self.que_num+=1
        self.q=input(f"Q.{self.que_num} {question.que} [TRUE/FALSE]?:")
    
    def answer(self):
        self.q==self.questions