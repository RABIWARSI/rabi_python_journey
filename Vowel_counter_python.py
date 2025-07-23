text = "Allah will help me"
vowels = "aeiou"
count = 0

for c in text:
    if c in vowels:
        count += 1

print("Total number of vowels:", count)
