def km_to_miles(km):
    return km*0.621371

def miles_to_km(miles):
    return miles/0.620371

def c_to_f(celsius):
    return (celsius*9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit-32) * 5/9

while True:
    print(" Unit converter")
    print("1.kilometers to miles")
    print("2.miles to kilometer")
    print("3.celsius to fahreenheit")
    print("4.fahrenheit to celsius")
    print("5.exit")
    

    try:
        choice = int(input("enter your choice : "))
        if choice==1:
            km = float(input("enter kilometer value : "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")

        elif choice==2:
            miles = float(input("enter miles value : "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} kilometer")
            
        elif choice==3:
            celsius = float(input("enter celsius value : "))
            print(f"{celsius} celsius = {c_to_f(celsius):.2f} f")

        elif choice==4:
            fahrenheit=float(input("enter fahrenheit value : "))
            print(f"{fahrenheit} fahrenheit  = {f_to_c(fahrenheit):.2f} c")
                    
        elif choice==5:
            break
            
    except ValueError:
        print("enter valid input")