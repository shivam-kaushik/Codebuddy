from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that teaches programming concepts."},
            {"role": "user", "content": user_message}
        ]
    )
    
    bot_response = response.choices[0].message.content
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)

print("Make sure to set your OPENAI_API_KEY environment variable!")

