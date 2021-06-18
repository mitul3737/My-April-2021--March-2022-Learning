F = open("input1.txt", "w")
F.write("Hello\nWorld")
F.close()
lines = []
for line in open("input1.txt"):
    lines.append(line.strip())
print(lines)