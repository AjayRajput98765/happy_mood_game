from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__)

# Load happy advice data
with open('data/advice.json', encoding='utf-8') as f:
    advice_list = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    selected_card = request.form.get('card')
    random_advice_data = random.choice(advice_list)

    return render_template(
        'result.html',
        card=selected_card,
        advice=random_advice_data['text'],
        character_name=random_advice_data['character'],
        character_video=random_advice_data['video']
    )


if __name__ == '__main__':
    app.run(debug=True)
