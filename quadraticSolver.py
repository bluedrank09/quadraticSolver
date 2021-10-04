import sys
import logging as log
import inspect
import cmath

def printOutput(quadRoot):
    try:
        print(quadRoot)

    except Exception as error : 
        print(error)
        raise error
    

def findRoots(cfxs, coeff, constant):
    try:
        print(f"{cfxs}")
        print(f"{coeff}")
        print(f"{constant}")

        quadRoot = ((coeff*-1)+(cmath.sqrt(coeff*coeff - (4*cfxs*constant))))/2*cfxs

        printOutput(quadRoot)
    
    except Exception as error : 
        print(error)
        raise error

def parseInput(formula):
    try: 
        variables = []
        variables = formula.split("+", 3)
        
        cfxsString = variables[0]
        coeffString = variables[1]
        constantString = variables[2]

        cfxs = int(cfxsString[0])
        coeff = int(coeffString[0])
        constant = int(constantString)

        findRoots(cfxs,coeff,constant)
    
    except Exception as error : 
        print(error)
        raise error

def getUserInput():
    try:
        userInput = input(f"Give me a quadratic equation (e.g 3x^2 + 6x + 5 = 0) :")
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