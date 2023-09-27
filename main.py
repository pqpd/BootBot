with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
count = len(words)
dict = {}
for word in words:
    for char in word:
        if char.isalpha():
            if char.lower() in dict:
                dict[char.lower()] += 1
            else:
                dict[char.lower()] = 1
sorted_dict = sorted(dict.items(),key=lambda item: item[1], reverse=True)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count} words found in the document")
print(" ")
for key, value in sorted_dict:
    print(f"The '{key}' character was found {value} times")

print("--- End report ---")
