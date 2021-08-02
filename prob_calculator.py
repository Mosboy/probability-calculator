import copy
import random
# Consider using the modules imported above.

class Hat:
   
    def __init__(self, **balls):
        self.initial_contents = []#this will contain all the initial balls even if it is selected incase of another experiment is taken
        self.contents = []
        for name_of_balls in balls: 
            no_of_balls = []
            for i in range(0, int(balls[name_of_balls])):
                self.initial_contents.append(name_of_balls)
                self.contents.append(name_of_balls)
        

    def draw(self, num_balls_drawn):
       self.contents = copy.copy(self.initial_contents)#passing all the initial balls the contents list for new experiments
       if(num_balls_drawn > len(self.contents)):#if the num of balls to be drawn is more than the available balls, it should return all
           balls_drawn = self.contents

       else:#this will randomly select/remove balls from the self.contents
           balls_drawn = []
           for i in range(0, num_balls_drawn):
               get_random = random.randint(0, len(self.contents)-1)#getting the random index 
               balls_drawn.append(self.contents[get_random])#passing the ball selected to the ball_drawn list
               del self.contents[get_random]#removing the ball selected from self.contents
       return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
    No_of_outcome = 0#this will count how many times our event occurs
    for i in range(0, num_experiments):  
        balls_drawn = hat.draw(num_balls_drawn)#get the list of all the balls that is drawn randomly
        check = []#check if true of false a required event has taken place e.g if it contains atleast 2 red and 1 green.
        for name_of_expected_balls in expected_balls:
            a = balls_drawn.count(name_of_expected_balls) >= expected_balls[name_of_expected_balls]#return a boolean if our event occurs
            check.append(a)
        if(check.count(False) == 0):
            No_of_outcome += 1

    probability = No_of_outcome/num_experiments#calculate our probability
    return probability