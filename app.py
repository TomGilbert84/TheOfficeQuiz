import os
from flask import Flask, render_template, request, send_from_directory
import random
from datasets import load_dataset

dataset = load_dataset("jxm/the_office_lines")
speakers = list(set(example["speaker"] for example in dataset["train"]))

app = Flask(__name__)


@app.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'static'), path)


@app.route('/')
def quiz():
    # Select a random line spoken by one of the characters in speakers
    lines = [example["line_text"]
             for example in dataset["train"] if example["speaker"] in speakers]
    random_line = random.choice(lines)

    # Get the character who said the line
    index = dataset["train"]["line_text"].index(random_line)
    character = dataset["train"][index]["speaker"]

    # Randomly select four characters, including the correct answer
    answer_options = random.sample(speakers, k=3) + [character]
    random.shuffle(answer_options)

    # Generate the question
    question = f"Which character said the following line: '{random_line}'?"

    # Render the template with the question and possible answers
    return render_template('quiz.html', question=question, answer_options=answer_options)


@app.route('/', methods=['POST'])
def check_answer():
    # Get the user's answer
    user_answer = request.form['answer']

    # Select a random line spoken by one of the characters in speakers
    lines = [example["line_text"]
             for example in dataset["train"] if example["speaker"] in speakers]
    random_line = random.choice(lines)

    # Get the character who said the line
    index = dataset["train"]["line_text"].index(random_line)
    character = dataset["train"][index]["speaker"]

    # Check if the user's answer is correct
    if user_answer.lower() == character.lower():
        result = "Correct!"
    else:
        result = f"Incorrect! The correct answer is {character}."

    # Render the template with the result and a new question
    return render_template('results.html', result=result, speakers=speakers)
