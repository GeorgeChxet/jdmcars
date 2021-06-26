from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/nissan')
def nissan():
    return render_template("nissan.html")

@app.route('/toyota')
def toyota():
    return render_template("toyota.html")

@app.route('/subaru')
def subaru():
    return render_template("subaru.html")

@app.route("/mitsubishi")
def mitsubishi():
    return render_template("mitsubisi.html")



@app.route("/subscribe", methods =['POST'])
def subscribe():
    name = request.form['name']
    secondname = request.form['secondname']
    email = request.form['email']
    return render_template("subscribe.html", name = name.capitalize())

if __name__ == '__main__':
    app.run(debug = True)