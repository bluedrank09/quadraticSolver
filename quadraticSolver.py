import sys
import logging as log
import inspect

def printInput():
    pass

def findRoots():
    pass

def parseInput():
    pass

def getUserInput():
    userInput = input(f"Give me a quadratic equation (e.g 3x^2 + 6x + 5 = 0) :")
    return(userInput)

if __name__ == "__main__":
    try:
        print(getUserInput())

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":)")