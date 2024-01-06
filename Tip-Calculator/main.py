try:
    food_amount = float(input("Enter your food amount $: "))
    tip_percentage = float(input("Enter tip percentage: %")) / 100

    tip_amount = food_amount * tip_percentage
    total = food_amount + tip_amount

    print('\n\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Tip amount ${tip_amount}')
    print(f'Food amount ${food_amount}')
    print('\n')
    print('Total: ${:.2f}'.format(total))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

except ValueError:
    print("Please enter valid numeric input.")
