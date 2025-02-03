user_name = input('Enter user name: ')
plan = input('Enter plan (e.g., normal, prime): ')
user_id = int(input('Enter your ID: '))
lst = [111, 222, 444]
if plan == 'prime' and user_id in lst:
    print(f"Hello {user_name}, you are a prime member!")
    num_tickets = int(input('Enter number of tickets to book: '))
    ticket_price = float(input('Enter the price of one ticket: '))  
    total_price = num_tickets * ticket_price
    discount_percentage = 20
    discount_amount = total_price * (discount_percentage / 100)
    final_price = total_price - discount_amount
    print(f"Total price before discount: ${total_price}")
    print(f"Discount applied ({discount_percentage}%): -${discount_amount}")
    print(f"Final price after discount: ${final_price}")
    
else:
    print('Invalid prime user or not a prime plan member.')
