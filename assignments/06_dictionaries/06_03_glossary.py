# Glossary of 5 programming words (keys) with their meanings (values)
glossary = {
	"variable": "A named location used to store data in memory.",
	"function": "A reusable block of code that performs a specific task and can be called with arguments.",
	"loop": "A control structure that repeats a block of code until a condition is met.",
	"list": "An ordered, mutable collection of items.",
	"dictionary": "A collection of key-value pairs for fast lookup by key."
}

# Print each word and its meaning
for word, meaning in glossary.items():
	print(f"{word}: {meaning}") # print each word and its meaning 
# Print the entire glossary
print("\nComplete Glossary:")
print(glossary) # print the entire dictionary
