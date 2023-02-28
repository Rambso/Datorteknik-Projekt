from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/dicer", methods = ["GET", "POST"])
def dice():
    if request.method == "POST":
        amm = int(request.form.get("ammount"))
        side = int(request.form.get("sides"))
        bon = int(request.form.get("append"))
        results = []
        for roll in range(amm):
            results.append(random.randint(1, side))
        sults = sum(results) + bon
        return render_template('dicer.html') + "You rolled: " + str(results) + " + " + str(bon) + " = " + str(sults)
    return render_template('dicer.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
