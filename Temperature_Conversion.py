#Example 1:- Temperature Conversion

def temp_conversion(temp, unit):
    """This function convert temperature between celsius and fahrenheit"""
    if unit=='C':
        return temp *9/5+32 #celsius to fahrenheit
    elif unit=='F':
        return (temp-32)*5/9 # Fahrenheit to celsius
    else:
        return None

print(temp_conversion(25,'C')) 
print(temp_conversion(56,'F')) 