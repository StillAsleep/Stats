# -*- coding: utf-8 -*-
"""
Name: Muhammad Taha Sheikh
Program: Online Statistics

Description: Program asks for non-negative numbers and returns the mean and variance 
Program ends when a negative number is entered.

"""

class OnlineStats:
    
    
    def __init__(self):
        """
        Initializes the OnlineStats object with a mean, variance and the total number
        of numbers entered
        
        """
        self.mean = 0
        self.variance = 0
        self.n = 0
        
    def calculate_mean_and_variance(self, x):
        """
        Calculates the mean and variance once given a number x.
        
        Input: x or number a user enters
        Output: Mean and Variance of said number
        
        """
        previous_mean = self.mean # Remembers the previous number entered
        self.n = self.n + 1 # With Every number added the count goes up
        
        self.mean = previous_mean + ((x - previous_mean) / float(self.n))
                
        previous_variance = self.variance
        
        if self.n > 1:
            self.variance = ((self.n - 2)/float((self.n - 1)) * 
                             previous_variance + (x - previous_mean)**2 / self.n)
        
        return (self.mean, self.variance)
    
    def statistics(self, inp, out):
        """
        Puts the calculated mean and variance into a tuple to be accessible by
        "__main__".
        
        """
        online_stats = OnlineStats()
        x = inp()
    
        while (x >= 0): # As long as the number entered is not negative it will continue
            stats = online_stats.calculate_mean_and_variance(x)
            out(stats[0], stats[1]) # Tuple created
            x = inp()
            
            
def console_input():
    """
    Asks user to enter a number, exits if negative number is added or raises 
    exception if a number is not added
    """
    while True:
        try:
            x = float(input("Enter a number: "))
            if x<0:
                print ("You have entered a negative number, the calculation will now stop")
                raise SystemExit()
            else:    
                return x;
        except ValueError:  # Just in case someone enters a letter
            print ("Please enter numeric values only.")

def console_output(mean, variance):
    """
    Outputs mean and variance as asked by prompt
    """
    
    print ("Mean is " + str(mean) +" variance is " + str(variance))

if __name__ == "__main__":
# Print heading info
    print ("NAME: Muhammad Taha Sheikh")
    print ("ASSIGNMENT #1")    
           
    # Initializes Class and tells it to put in console_input and console_output
    # as inp and out       
    OnlineStats().statistics(console_input, console_output)