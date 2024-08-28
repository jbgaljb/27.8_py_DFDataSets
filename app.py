from enum import Enum
import pandas as pd

class DataSet(Enum):
    JOB_POSTINGS = 1
    TRIVIA_QUESTIONS = 2
    NYC_SQUIRRELS = 3

class Operations(Enum):
    INFO = 1
    HEAD = 2
    TAIL = 3

def workYourMagic(chosenSetDF, operationEnum):
    operation = (operationEnum.name).lower()
    print(getattr(chosenSetDF, operation)())

def menu1():
    for set in DataSet:
        print(f"{set.name} - {set.value}")
    # returns chosen data set
    return int(input("choose from the following options data sets one "))

def menu2():
    for op in Operations:
        print(f"{op.name} - {op.value}")
    # returns chosen data set
    return int(input("choose from the following options data sets one "))

def load(dataSet):
    file_name = f"{dataSet.name.lower()}.csv"
    try:
        dataF = pd.read_csv(file_name)
        print(f"Successfully loaded {file_name}")
        return dataF
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return None
    
def main():
    while True:
        setNumber = menu1() # number of chosen set
        chosenSetDF = load(DataSet(setNumber))
        chosenOpNum = menu2()
        workYourMagic(chosenSetDF, Operations(chosenOpNum))

if __name__ == '__main__':
    main()