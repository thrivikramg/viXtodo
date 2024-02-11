
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=enumerate(tasks))

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('i')
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/pop/<int:index>', methods=['POST'])
def pop_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


