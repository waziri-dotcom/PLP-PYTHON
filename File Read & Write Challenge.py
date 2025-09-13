with open("input.txt", "r") as infile:
    content = infile.read()


modified_content = content.upper()

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("Modified content written to output.txt ✅")
