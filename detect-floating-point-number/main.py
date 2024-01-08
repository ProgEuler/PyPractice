def is_valid_float(N):
    try:
        # Attempt to convert the string to a float
        float_value = float(N)

        # Check if the string starts with +, -, or .
        if N[0] in ['+', '-', '.']:
            # Check if there is a decimal value
            if '.' in N:
                # Check if there is exactly one '.' symbol
                if N.count('.') == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    except ValueError:
        # If conversion to float raises an exception, it's not a valid float
        return False

# Input the number of test cases
num_test_cases = int(input().strip())

# Process each test case
for _ in range(num_test_cases):
    input_string = input().strip()
    result = is_valid_float(input_string)
    print(result)
