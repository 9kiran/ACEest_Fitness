from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)
workouts = []

html_template = """
<!doctype html>
<html>
  <head><title>ACEest Fitness</title></head>
  <body>
    <h1>ACEest Fitness Tracker</h1>
    <form method="POST" action="/add">
      <label>Workout:</label>
      <input type="text" name="workout" required>
      <br>
      <label>Duration (minutes):</label>
      <input type="number" name="duration" required>
      <br><br>
      <button type="submit">Add Workout</button>
    </form>
    <h2>Logged Workouts</h2>
    <ul>
      {% for w in workouts %}
        <li>{{ loop.index }}. {{ w['workout'] }} - {{ w['duration'] }} mins</li>
      {% endfor %}
    </ul>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(html_template, workouts=workouts)

@app.route("/add", methods=["POST"])
def add_workout():
    workout = request.form.get("workout")
    duration = request.form.get("duration")

    if not workout or not duration:
        return "Error: Workout and duration required", 400

    try:
        duration = int(duration)
    except ValueError:
        return "Error: Duration must be a number", 400

    workouts.append({"workout": workout, "duration": duration})
    return redirect(url_for("home"))

if __name__ == "__main__":  # pragma: no cover
    app.run(host="0.0.0.0", port=5000)
