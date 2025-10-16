print("flying broomsticks")  
broomstick = ["Nimbus 2000", "Firebolt", "Cleansweep 7", "Comet 260"]
print(broomstick)
print(broomstick[0])
print(broomstick[1])
print(broomstick[2])
print(broomstick[3])
print(f"I would like to own a {broomstick[0]} broomstick")
print(f"I would like to own a {broomstick[1]} broomstick")
print(f"I would like to own a {broomstick[2]} broomstick")
print(f"I would like to own a {broomstick[3]} broomstick")
broomstick[0] = "Firebolt"
print(broomstick)
broomstick.append("Silver Arrow")
print(broomstick)
broomstick.insert(0, "Thunderbolt")
print(broomstick)
del broomstick[2]
print(broomstick)
popped_broomstick = broomstick.pop()
print(broomstick)
print(popped_broomstick)
broomstick.remove("Cleansweep 7")
print(broomstick)
too_expensive = "Firebolt"
broomstick.remove(too_expensive)
print(broomstick)
print(f"A {too_expensive} is too expensive for me.")
print(broomstick)
broomstick.sort()
print(broomstick)
broomstick.sort(reverse=True)
print(broomstick)
print(sorted(broomstick))
print(broomstick)
broomstick.reverse()
print(broomstick)
print(len(broomstick)) 
print("The first three broomsticks in my list are:")
for broom in broomstick[:3]:
    print(broom)
print("Three broomsticks from the middle of my list are:")
for broom in broomstick[1:4]:
    print(broom)
print("The last three broomsticks in my list are:")
for broom in broomstick[-3:]:
    print(broom)
my_brooms = broomstick[:]
print("My friend's broomsticks are:")
friend_brooms = my_brooms
friend_brooms.append("Elder Wand")
print("My broomsticks:")
print(my_brooms)
print("My friend's broomsticks:")
print(friend_brooms)
print("My favorite broomsticks are:")
for broom in broomstick:
    print(broom)
print("My favorite broomsticks are:")
for broom in broomstick:
    print(broom.title())
print("My favorite broomsticks are:")
for broom in broomstick:
    print(f"{broom.title()}, is a great broomstick!")
print("My favorite broomsticks are:")
for broom in broomstick:
    print(f"I would like to own a {broom.title()} broomstick.")