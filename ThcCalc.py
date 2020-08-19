from os import system, name 
import math
def tc(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def quot(a,b):
    return a/b

def multi(a,b):
    return a*b

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        
def main():
    print("THC calculator")
    print("Enter THC % (ie 24.32 or 25.1): ")
    THCperc = input()
    resTHCperc = quot(float(THCperc),.100)
    oneg = resTHCperc               #quot(float(THCperc), .100)
    halfg = quot(float(resTHCperc),2)       #halfg = quot(oneg, 2)
    qrterg = quot(float(resTHCperc),4)      #quot(halfg, 2)
    onetenth = quot(float(resTHCperc),10)   #quot(oneg, 10)
    halfatenth = quot(float(resTHCperc),20) #quot(onetenth, 2)

    akilo = tc(multi(float(oneg),1000),2) #kilogram (1000 grams)
    anoz = tc(multi(float(oneg),28),2) #an ounce (28 grams)
    aqp = tc(multi(float(anoz),4),2) #quarter pound (112 grams)
    ahalfp = tc(multi(float(aqp),2),2) #half pound (224 grams)
    apound = tc(multi(float(ahalfp),2),2) #a pound (448 grams)
    ahalfz = tc(multi(float(oneg),14),2) #half ounce (14 grams)
    aqrter = tc(multi(float(oneg),7),2) #quarter ounce (7 grams)
    an8th = tc(multi(float(oneg),3.5),2) #an eighth (3.5 grams)

    print("THC Results:\nA Kilogram (1000 grams = 2.23 Pounds): ",akilo," mg\nA Pound (448 grams = 16 Ounces): ",apound," mg\nA Half Pound (8 Ounces = 224 grams): ", ahalfp," mg\nA Quarter Pound (4 Ounces = 112 grams): ",aqp, " mg\nAn Ounce (28g = 28000mg): ",anoz," mg\nA Half Ounce (14g = 14000mg): ",ahalfz," mg\nA quarter ounce (7g = 7000mg): ",aqrter," mg\nAn 8th (3.5g = 3500mg): ",an8th," mg\nOne gram (1g = 1000mg): ", oneg, " mg\nHalf Gram (0.5g = 500mg): ",halfg," mg\nQuarter Gram (0.25g = 250mg): ",qrterg," mg\nOne Tenth (0.1g = 100mg): ",onetenth," mg\nHalf a Tenth (0.05g = 50mg): ", halfatenth, " mg\n")
    input("Press any key to continue (will clear results)...")
    clear()
    main()
    
if __name__ == '__main__':
   main()