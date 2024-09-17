def c_to_f(cel):
    f=(cel * 9/5) + 32
    return f
def f_to_c(fahr):
    c=(fahr - 32) * 5/9
    return c
def main():
    c=0
    while(c==0 or c==1 or c==2):
        print("+++++++++TEMPRATURE CONVERTER++++++++++")
        print("1. CELSIUS TO FAHRENHEIT")
        print("2. FAHRENHEIT TO CELSIUS")
        c=int(input("ENTER YOUR CHOICE :"))
        if(c==1):
            cel=float(input("enter temprature in celsius :"))
            print("temprature in fahrenheit is : ",c_to_f(cel))
        if(c==2):
            fahr=float(input("enter temprature in fahrenheit :"))
            print("temprature in celsius is : ",f_to_c(fahr))
main()
    

"""
Output:-


PS D:\cognifyz\L1> Python L1T2.py
+++++++++TEMPRATURE CONVERTER++++++++++
1. CELSIUS TO FAHRENHEIT
2. FAHRENHEIT TO CELSIUS
ENTER YOUR CHOICE :1
enter temprature in celsius :25
temprature in fahrenheit is :  77.0
+++++++++TEMPRATURE CONVERTER++++++++++
1. CELSIUS TO FAHRENHEIT
2. FAHRENHEIT TO CELSIUS
ENTER YOUR CHOICE :2
enter temprature in fahrenheit :77
temprature in celsius is :  25.0
+++++++++TEMPRATURE CONVERTER++++++++++
1. CELSIUS TO FAHRENHEIT
2. FAHRENHEIT TO CELSIUS
ENTER YOUR CHOICE :1
enter temprature in celsius :80
temprature in fahrenheit is :  176.0
+++++++++TEMPRATURE CONVERTER++++++++++
1. CELSIUS TO FAHRENHEIT
2. FAHRENHEIT TO CELSIUS
ENTER YOUR CHOICE :2
enter temprature in fahrenheit :176
temprature in celsius is :  80.0
+++++++++TEMPRATURE CONVERTER++++++++++
1. CELSIUS TO FAHRENHEIT
2. FAHRENHEIT TO CELSIUS
ENTER YOUR CHOICE :


"""