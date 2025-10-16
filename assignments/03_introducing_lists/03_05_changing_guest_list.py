spellcaster = "newton" 
teacher = "mr smith"
magician = "harry potter"
guests = ['ali', 'ahmed', 'sara', 'mona', spellcaster, teacher]
print("Initial guest list:")
print(guests)
print("\nInviting guests to dinner:")
for guest in guests:
    print(f"Dear {guest.title()}, you are cordially invited to dinner at my place.")
print("\nUnfortunately, I can only invite two people for dinner.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Dear {removed_guest.title()}, I regret to inform you that I can no longer invite you to dinner.")
print("\nGuests still invited to dinner:")
for guest in guests:
    print(f"Dear {guest.title()}, you are still invited to dinner at my place.")
del guests[0]
del guests[0]
print("\nFinal guest list (should be empty):")
print(guests)
print(f"\nNumber of guests still invited: {len(guests)}") 