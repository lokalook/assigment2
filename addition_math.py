import random

MIN_NUM = 10
MAX_NUM = 99
row = 0

def main():
    """
    Pre Condition: Generate random number. Additional num 1 and num 2
    Post Condition : Check user answers. If answer correct add row if incorrect reset row to zero 
    """
    row = 0
    while row < 3:
        # number generator
        num_1 = random.randint(MIN_NUM, MAX_NUM)
        num_2 = random.randint(MIN_NUM, MAX_NUM)
        print("What is " + str(num_1) + " + " + str(num_2) + " ?")
        total = num_1 + num_2
        #user answer
        user_input = int(input("Your answer: "))
        # Check user answer
        # if answer is incorrect, reset row to zero
        if user_input == total:
            row += 1
            print("Correct!  You've gotten " + str(row) +" correct in a row ")
        else:
            print("Incorrect. The expected answer is " + str(total))
            row = 0    

if __name__ == "__main__":
    main()    
