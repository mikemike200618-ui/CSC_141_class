guests =['ali', 'ahmed', 'sara', 'mona', 'newton', 'mr smith',] 
print("Initial guest list:") 
print(guests)
print("\nInviting guests to dinner:")
for guest in guests:
    print(f"Dear {guest.title()}, you are cordially invited to dinner at my place.")
newton = "newton"
guests[4] = newton
print("\nUpdated guest list after replacing a guest:")
print(guests)
print("\nInviting guests to dinner after updating the list:")
for guest in guests:
    print(f"Dear {guest.title()}, you are cordially invited to dinner at my place.")
print("\nGood news! I found a bigger dinner table.")
guests.insert(0, 'lina')
guests.insert(3, 'omar')
guests.append('fatima')
print("\nGuest list after adding more guests:")
print(guests)
print("\nInviting guests to dinner after adding more guests:")
for guest in guests:
    print(f"Dear {guest.title()}, you are cordially invited to dinner at my place.")