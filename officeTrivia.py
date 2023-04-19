import random
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("jxm/the_office_lines")

# Define a function to select a random line spoken by one of the characters in speakers


def select_random_line(speakers):
    lines = [example["line_text"]
             for example in dataset["train"] if example["speaker"] in speakers]
    return random.choice(lines)


# Get a list of unique speaker names from the dataset
speakers = list(set(example["speaker"] for example in dataset["train"]))

# Print the list of speaker names
print("Characters in the dataset:", ", ".join(speakers))

# Generate a question
question = "Which character said the following line: "

# Select a random line spoken by one of the characters in speakers
random_line = select_random_line(speakers)

# Get the character who said the line
index = dataset["train"]["line_text"].index(random_line)
character = dataset["train"][index]["speaker"]

# Add the character to the question
question += f'"{random_line}"?'

# Print the question
print(question)

# Get the user's answer
while True:
    user_answer = input("Enter your answer: ")
    if user_answer.lower() in (speaker.lower() for speaker in speakers):
        break
    else:
        print("Invalid answer. Please try again.")

# Check if the user's answer is correct
if user_answer.lower() == character.lower():
    print("Correct!")
else:
    print(f"Incorrect! The correct answer is {character}.")
