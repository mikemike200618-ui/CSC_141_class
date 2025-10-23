print("a list called sandwich_orders with the names of various sandwiches.") 
sandwich_orders = ['turkey', 'ham', 'roast beef', 'veggie', 'tuna']
finished_sandwiches = []    
print("i made your turkey sandwich.") 
finished_sandwiches.append('turkey')
print("i made your ham sandwich.")
finished_sandwiches.append('ham')
print("i made your roast beef sandwich.")
finished_sandwiches.append('roast beef')
print("i made your veggie sandwich.")
finished_sandwiches.append('veggie')
print("i made your tuna sandwich.")
finished_sandwiches.append('tuna')  
print("list called finished_sandwiches to store the names of the sandwiches that have been made.") 
print("The following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}") 
print("i made your tuna sandwich.")
finished_sandwiches.append('tuna')
print("list called finished_sandwiches to store the names of the sandwiches that have been made.")
print("The following sandwiches have been made:") 
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")  