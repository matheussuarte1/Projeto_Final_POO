from flask import Flask, render_template, request, redirect, url_for
from models.activity import WorkActivity, StudyActivity, PersonalActivity
from models.strategies import SortByDateStrategy, SortByPriorityStrategy
from models.observer import ConsoleNotifier
from models.agenda import Agenda
from models.factory import ActivityFactory

app = Flask(__name__)

# Agenda e estratégia padrão
agenda = Agenda(strategy=SortByDateStrategy())
notifier = ConsoleNotifier()
agenda.attach(notifier)

@app.route("/sort/date")
def sort_by_date():
    agenda.strategy = SortByDateStrategy()
    return redirect(url_for("index", sort="date"))


@app.route("/sort/priority")
def sort_by_priority():
    agenda.strategy = SortByPriorityStrategy()
    return redirect(url_for("index", sort="priority"))

@app.route("/")
def index():
    current_sort = request.args.get("sort", "date")
    tasks = agenda.get_sorted_activities()
    return render_template("index.html", tasks=tasks, current_sort=current_sort)


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        priority = int(request.form["priority"])
        activity_type = request.form["activity_type"]

        # Criação do objeto correto conforme o tipo
        activity = ActivityFactory.create_activity(
        activity_type, title, description, deadline, priority
        )
        # Adiciona à agenda
        agenda.add_activity(activity)

        return redirect(url_for("index"))

    return render_template("add_task.html")


if __name__ == "__main__":
    app.run(debug=True)

