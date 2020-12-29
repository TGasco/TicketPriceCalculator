#Student ID: 201419827      Gascoyne_Thomas-CA06.py
#November 2019
#Program to calculate the sale price for plane tickets to turn a desired profit

from random import randint

def main():
    Count = 0
    Welcome()
    FirstPriceList = []
    EcoPriceList = []
    OperatingCost = float(input("\nInput the operating cost of the flight: £"))
    ProfitMargin = float(input("\nInput the desired profit margin percentage: "))
    DrinkWholesale = float(input("\nInput the wholesale price of 1 drink: £"))
    
    ProfitMarginDec = Decimal(ProfitMargin)
    FullFlight(OperatingCost, ProfitMarginDec, DrinkWholesale, Count,
               EcoPriceList, FirstPriceList)
    for i in range(5):
        Count += 1
        PartialFlight(OperatingCost, ProfitMarginDec, DrinkWholesale, Count,
                  EcoPriceList, FirstPriceList)
    return



def Welcome():
    Welcome = input("Welcome! This program is used to calculate the costs"
                    "Associated with operating a flight, and can estimate"
                    "the best price to set tickets at for a desired profit"
                    "\n Press X to continue: ")
    while Welcome.upper() != "X":
        Welcome = input("\nPlease press X to continue: ")
    return



def MatrixInit(x):
    SeatPlan = [[x] * 5 for i in range(5)]
    return (SeatPlan)



def Decimal(ProfitMargin):
    ProfitMarginDec = (ProfitMargin / 100) + 1
    return (ProfitMarginDec)



def FullFlight(OperatingCost, ProfitMarginDec, DrinkWholesale, Count,
               EcoPriceList, FirstPriceList):
    SeatsFull = 25
    Flight = 0
    x = 1
    SeatPlan = MatrixInit(x)
    FirstClass = SeatPlan[0:2]
    EconomyClass = SeatPlan[2:5]

    Drinks(DrinkWholesale, OperatingCost, SeatPlan, Flight, Count, ProfitMarginDec,
           EcoPriceList, FirstPriceList, SeatsFull)
    
    return (OperatingCost, ProfitMarginDec, SeatPlan, DrinkWholesale, x)



def PartialFlight(OperatingCost, ProfitMarginDec, DrinkWholesale, Count,
                  EcoPriceList, FirstPriceList):
    Flight = "Partial"
    x = 0
    SeatPlan = MatrixInit(x)
    FirstClass = SeatPlan[0:2]
    EconomyClass = SeatPlan[2:5]
    SeatList = MatrixInit(x)
    
    SeatsFull = randint(12,24)
    for i in range(SeatsFull):
        RandRow = randint(0,4)
        RandCol = randint(0,4)
        
        if SeatPlan[RandRow][RandCol] == 0: 
            SeatPlan[RandRow][RandCol] = 1
            
        else:
            while SeatPlan[RandRow][RandCol] == 1:
                RandRow = randint(0,4)
                RandCol = randint(0,4)
            SeatPlan[RandRow][RandCol] = 1

    Drinks(DrinkWholesale, OperatingCost, SeatPlan, Count, Flight, ProfitMarginDec,
           EcoPriceList, FirstPriceList, SeatsFull)
    
    return (OperatingCost, ProfitMarginDec, DrinkWholesale, x)



def Drinks(DrinkWholesale, OperatingCost, SeatPlan, Count, Flight, ProfitMarginDec,
           EcoPriceList, FirstPriceList, SeatsFull):
    #Algorithm to randomly calculate who buys drinks - and how many
    DrinksSold = 0
    DrinkPrice = DrinkWholesale * 1.5
    
    for i in range(SeatsFull):
        x = 60
        count = 0
        RandNum = randint(1,100)
        
        while x <= 100 and RandNum >= x:
            if RandNum >= x:
                DrinksSold += 1
                count += 1
                x = x + (18 * count)
            else:
                pass
            
    DrinksRev = DrinksSold * DrinkPrice
    WholesaleTot = DrinkWholesale * DrinksSold
    BreakEven = OperatingCost + WholesaleTot

    TicketPrice(BreakEven, SeatPlan, Flight, Count, DrinksRev, ProfitMarginDec,
                EcoPriceList, FirstPriceList, DrinksSold)
    
    return (DrinksRev, WholesaleTot)


def TicketPrice(BreakEven, SeatPlan, Flight, Count, DrinksRev, ProfitMarginDec,
                EcoPriceList, FirstPriceList, DrinksSold):
    #Algorithm which calculates the recommended ticket price
    RowTot = [sum(i) for i in SeatPlan]
    FirstTot = sum(RowTot[0:2])
    EcoTot = sum(RowTot[2:5])
    RecommendedPrice = (((BreakEven - DrinksRev)*ProfitMarginDec) /
    (EcoTot + (2*FirstTot))
                        )
    RecommendedPrice1st = 2 * RecommendedPrice
    
    if Flight == 0:
        FullOutput(SeatPlan, BreakEven, ProfitMarginDec, RecommendedPrice,
                   RecommendedPrice1st, DrinksSold)
        
    elif Flight == "Partial":
        PartialOutput(Count, SeatPlan, BreakEven, ProfitMarginDec,
                  RecommendedPrice1st, RecommendedPrice, EcoPriceList,
                      FirstPriceList, DrinksSold)
        
    
    return RecommendedPrice, RecommendedPrice1st


def FullOutput(SeatPlan, BreakEven, ProfitMarginDec, RecommendedPrice,
               RecommendedPrice1st, DrinksSold):
    ProfitMargin = (ProfitMarginDec-1) * 100
    MatriceDisplay(SeatPlan)
    print("\nFor a full flight, with total operating cost " + "£" +
            f"{BreakEven:.2f}",
            "and desired\n profit margin of", f"{ProfitMargin:.1f}" + "%",
            "The recommended ticket prices would be:\n",
            "\n\t1st Class:" + "£" + f"{RecommendedPrice1st:.2f}\n",
            "\n\tEconomy Class:" + "£" + f"{RecommendedPrice:.2f}"
            "\n\nAssuming", DrinksSold,"drinks are sold")
    Continue = input("\nOnce reviewed, press any key to continue...")
    return




def PartialOutput(Count, SeatPlan, BreakEven, ProfitMarginDec,
                  RecommendedPrice1st, RecommendedPrice, EcoPriceList,
                  FirstPriceList, DrinksSold):
    
    ProfitMargin = (ProfitMarginDec-1) * 100
    
    FirstPriceList.append(RecommendedPrice1st)
    EcoPriceList.append(RecommendedPrice)
    MatriceDisplay(SeatPlan)
    
    print("\n\t1st Class:" + "£" + f"{RecommendedPrice1st:.2f}\n",
        "\n\tEconomy Class:" + "£" + f"{RecommendedPrice:.2f}"
        "\n\nAssuming", DrinksSold,"drinks are sold")
    Continue = input("\nOnce reviewed, press any key to continue...")
    
    if Count == 5: #Averages the 5 calulates prices
        AverageFirstClass = sum(FirstPriceList[0:5])/5
        AverageEcoClass = sum(EcoPriceList[0:5])/5
               
        print("\nFor a partial flight, with total operating cost " + "£" +
            f"{BreakEven:.2f}",
            "and desired\n profit margin of", f"{ProfitMargin:.0f}" + "%",
            "The average recommended ticket prices would be:\n",
            "\n\t1st Class:" + "£" + f"{AverageFirstClass:.2f}\n",
            "\n\tEconomy Class:" + "£" + f"{AverageEcoClass:.2f}")
    else:
        pass
    return


def MatriceDisplay(SeatPlan): #Function to visually display the matrix 
   
    for row in range(len(SeatPlan)):
        for column in range(len(SeatPlan[row])):
            print(SeatPlan[row][column],end="   ")
        print()
    return


main()
