numbers = [1,2,3,4,5]
letters = ['A', 'B', 'C', 'D', 'E']
phonetic = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]

print("Unpacking as we loop through the list")
for number, letter, word in zip(numbers, letters, phonetic):
    print(f"{number}. {letter}: {word}")

print("Using a single item from the zipped list")
for item in zip(numbers, letters, phonetic):
    number, letter, word = item
    print(f"{number}. {letter}: {word}")