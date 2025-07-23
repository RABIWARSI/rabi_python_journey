thought1 = input ("Enter thought number 1:")
thought2 = input ("Enter thought number 2:")
thought3 = input ("Enter thought number 3:")

with open("positive_thought_jar.txt", "w") as f:
    f.write(thought1 + "\n")
    f.write(thought2 + "\n")
    f.write(thought3 + "\n")

with open("positive_thought_jar.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print("Reminder:", line.strip())
