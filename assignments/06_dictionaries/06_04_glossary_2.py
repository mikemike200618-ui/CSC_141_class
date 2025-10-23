# I will add a glossary to the file 06_04_glossary.py
glossary = { 'car': 'a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor and able to carry a small number of people',
             'bike': 'a two-wheeled vehicle that a person rides by pushing on foot'
             'airplane' 'a powered flying vehicle with fixed wings and a weight greater than that of the air it displaces',
                'boat': 'a small vessel for traveling over water, propelled by oars, sails, or an engine', 
                'broomsticks': 'a long, thin stick with a brush at one end, used for sweeping' } 
print("Glossary terms and their definitions:")
for term, definition in glossary.items(): 
    print(f"{term.title()}: {definition}") 