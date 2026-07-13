from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

tasks = ["test1"]
@app.route("/")
def main():
    return render_template("index.html", tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('newTask')

    if new_task:
        tasks.append(new_task)

    return redirect(url_for('main'))


@app.route('/complete', methods=['POST'])
def complete_tasks():
    completed_tasks = request.form.getlist('taskCheckbox')
    print(completed_tasks)

    for index in map(int, completed_tasks):
        if 1 <= index <= len(tasks):
            tasks[index - 1] += " - Completed"

    return redirect(url_for('main'))


@app.route('/delete', methods=['POST'])
def delete_tasks():
    tasks_to_delete = request.form.getlist('taskCheckbox')
    tasks_to_delete.sort(reverse=True)  # Start deleting from the end to avoid index issues
    for index in map(int, tasks_to_delete):
        if 1 <= index <= len(tasks):
            del tasks[index - 1]
    return redirect(url_for('main'))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)