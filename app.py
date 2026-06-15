from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(
    api_key="AQ.Ab8RN6JbRwfqiaGB4llgn332qazkvoU8gKGG3_ZQQBoio1g8rg"
)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()
    user_message = data.get("message", "")

    prompt = f"""
    You are an AI Healthcare Assistant.

    Rules:
    - Provide general healthcare guidance.
    - Do not diagnose diseases.
    - Do not prescribe medicines.
    - Recommend consulting a doctor for serious symptoms.
    - Keep responses concise and easy to understand.

    User Question:
    {user_message}
    """

    try:
        response = model.generate_content(prompt)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        })


if __name__ == '__main__':
    app.run(debug=True)