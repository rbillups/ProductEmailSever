from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST', 'GET'])
def process_data():
    if request.method == 'POST':
        user_input = request.form.get('userInput')
        selected_option = request.form.get('selectedOption')

        # Process the user input and selected option here using Python
        # For example, you can print the data to the console
        print(f'User Input: {user_input}')
        print(f'Selected Option: {selected_option}')

        # You can also perform more complex logic or database operations here

        return "Data processed successfully"  # Return a response to the client



if __name__ == "__main__":
    app.run(debug=True)
