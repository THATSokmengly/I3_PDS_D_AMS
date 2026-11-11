 
# is_digit check true or false is it be the integer or not
# Like  text.is_digit() check for the string (text )is it be the digit or not
# .strip() remove the space afront of and behind from the string


# Part B — a safe converter
def safe_int(text):
    """Turn text into an int; return None when it is not a number."""
    text = text.strip()
    if text.lstrip("-").isdigit():         # "42" or "-42"  
        return int(text)                    # lstrip checks for negative or space that is it be the digit 
    try:        # for check condition are true or false if it is true then it will return the integer value        
        return int(float(text))            # "3.9" -> 3
    except ValueError:      # if the condition fails it display none
        return None                        # "abc", "", "12a"


for sample in ["42 ", " -8 ", "3.9", "abc", "1000.9999900" ,""]:
    print(repr(sample), "->", safe_int(sample))



