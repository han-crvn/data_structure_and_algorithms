from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')


@app.route('/contact')
def contact():
     return render_template('contact.html')

@app.route('/ToUpperCase', methods=['GET', 'POST'])
def to_upper_case():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/AreaOfCircle', methods=['GET', 'POST'])
def area_circle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            result = 3.1416 * (radius ** 2)
        except ValueError:
            result = "Invalid input"
    return render_template('area_of_circle.html', result=result)

@app.route('/AreaOfTriangle', methods=['GET', 'POST'])
def area_triangle():
    result = None
    if request.method == 'POST':
        try:
            height = float(request.form.get('height', 0))
            base = float(request.form.get('base', 0))
            result = (height * base) / 2
        except ValueError:
            result = "Invalid input"
    return render_template('area_of_triangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
