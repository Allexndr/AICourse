from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-course', methods=['POST'])
def generate_course():
    course_description = request.form['course_description']
    # Здесь можно добавить логику для генерации курса на основе course_description
    return f"Course structure for: {course_description}"

if __name__ == '__main__':
    app.run(debug=True)
