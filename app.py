from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Access form data
        input_values = [request.form[f'input{i}'] for i in range(1, 11)]
        print(input_values)  # Display form values in console
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
