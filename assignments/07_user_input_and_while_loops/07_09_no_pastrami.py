print("The deli has run out of pastrami.") 
sandwich_orders = ['turkey', 'ham', 'pastrami', 'roast beef', 'pastrami', 'veggie', 'tuna', 'pastrami']
finished_sandwiches = [] 
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich) 