def main ():
    fraction = input ("Input: ")
    percentage = convert(fraction)
    output = gauge(percentage)
    print(output)
    

def convert(fraction):
    try:
        x,y = fraction.split("/")
        x,y = int(x),int(y)
    except ValueError:
        raise ValueError(f"num and denom must be integers, got {fraction}")
    if x<0 or y<0:
        raise ValueError("num or denom cannot be negative")
    if y==0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x>y:
        raise ValueError("Fuel cannot be more than full tank")
    
    
    return round(x/y*100)
    
def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()