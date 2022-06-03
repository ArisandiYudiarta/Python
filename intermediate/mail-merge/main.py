# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Files containing the names
with open("Input/Names/invited_names.txt", "r") as names:
    result_names = names.readlines()
    finished_names = []
    for names in result_names:
        finished_names.append(names.replace("\n", ""))
    # print(finished_names)

# Saving the finished file
for n in finished_names:
    # print(n)
    # Base Letter Template
    with open(f"Input/Letters/starting_letter.txt") as base:
        result_template = base.read()
        # print(result_template)
    # Writing the text
    with open(f"Output/ReadyToSend/invitation_{n.lower()}.txt", "w") as result:
        finished_template = result_template.replace("[name]", f"{n}")
        result.write(finished_template)
