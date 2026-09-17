def analyze_digits_and_case(user_input):
    if not user_input:
        return (0, 0)
    
    cleaned_input = user_input.strip()
    
    uppercase_count = 0
    digit_sum = 0
    
    for char in cleaned_input:
        if char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_sum += int(char)
            
    return (uppercase_count, digit_sum)