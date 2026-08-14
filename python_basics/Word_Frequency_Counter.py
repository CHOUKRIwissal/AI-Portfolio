sentence = input("ENTER your sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nWord frequency:")

for word, count in sorted_frequency:
    print(word, count)

print("\nTop 5 most frequent words:")

for word, count in sorted_frequency[:5]:
    print(word, count)