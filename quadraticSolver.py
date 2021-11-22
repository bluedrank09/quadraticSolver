import sys
import logging as log #importing a logger in case things go wrong and I need to keep track of it
import inspect
import cmath #importing a special maths package that is able to do quadratics

def printOutput(quadRoot):
    try:
        print(quadRoot)

    except Exception as error : 
        print(error)
        raise error
    

def findRoots(cfxs, coeff, constant):
    try:
        #printing out the main parts of the quadratic equatoin the user has given
        print(f"Coefficent of x sqaured is {cfxs}") 
        print(f"Coefficient of x is {coeff}")
        print(f"Constant is {constant}")

        quadRootOne = ((coeff*-1)+(cmath.sqrt(coeff*coeff - (4*cfxs*constant))))/2*cfxs #using the positive  quadratic formula to calculate the first root
        printOutput(f"Quadratic Root One Real : {(float(quadRootOne.real))*-1:.2f}, Quadratic Root One Imaginary : {float(quadRootOne.imag):.2f}")
        quadRootTwo = ((coeff*-1)-(cmath.sqrt(coeff*coeff - (4*cfxs*constant))))/2*cfxs #using the negative quadtaric formula to calculate the second root
        printOutput(f"Quadratic Root Two Real : {(float(quadRootTwo.real))*-1:.2f}, Quadratic Root Two Imaginary : {float(quadRootTwo.imag):.2f} ")
    
    except Exception as error : 
        print(error)
        raise error

def parseInput(formula):
    try: 
        #splitting at the + signs so it can get the different parts needed from the equation
        variables = []
        variables = formula.split("+", 3)
        
        cfxsString = variables[0]
        coeffString = variables[1]
        constantString = variables[2]

        #naming each part of the equation so that the somputer can use them in the calculation
        cfxs = int(cfxsString[0])
        coeff = int(coeffString[0])
        constant = int(constantString)

        findRoots(cfxs,coeff,constant)
    
    except Exception as error : 
        print(error)
        raise error

def getUserInput():
    try:
        userInput = input(f"Give me a quadratic equation (e.g 3x^2 + 6x + 5 = 0) :") #asking the user for an equation
        parseInput(userInput) 

    except Exception as error : 
        print(error)
        raise error

if __name__ == "__main__":
    try:
        getUserInput()

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":)")