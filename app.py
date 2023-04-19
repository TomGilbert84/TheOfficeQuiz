import secrets
import os
from flask import Flask, render_template, request, send_from_directory, session
import random
from datasets import load_dataset

dataset = load_dataset("jxm/the_office_lines")
speakers = list(set(example["speaker"] for example in dataset["train"]))


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


@app.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'static'), path)


@app.route('/')
def quiz():
    # Select a random line spoken by any character in the dataset
    example = random.choice(dataset["train"])

    # Save the line and character as session variables
    session['line_text'] = example['line_text']
    session['speaker'] = example['speaker']

    # Generate the question
    question = f"Which character said the following line: '{example['line_text']}'?"

    # Randomly select four characters, including the correct answer
    answer_options = random.sample(speakers, k=3) + [example['speaker']]
    random.shuffle(answer_options)

    # Render the template with the question and possible answers
    return render_template('quiz.html', question=question, answer_options=answer_options)


@app.route('/', methods=['POST'])
def check_answer():
    # Get the user's answer
    user_answer = request.form['answer']

    # Get the saved line and character from the session variables
    line_text = session.get('line_text')
    speaker = session.get('speaker')

    # Check if the user's answer is correct
    if user_answer.lower() == speaker.lower():
        result = "Correct!"
    else:
        result = f"Incorrect! The correct answer is {speaker}."

    # Render the template with the result and a new question
    return render_template('results.html', result=result, speakers=speakers)
