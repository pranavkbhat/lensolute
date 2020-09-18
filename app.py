from flask import Flask, render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nature')
def nature():
    return render_template('nature.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/people')
def people():
    return render_template('people.html')

@app.route('/wedding')
def wedding():
    return render_template('wedding.html')

@app.route('/motion')
def motion():
    return render_template('motion.html')

if __name__ == "__main__":
    app.run(debug=True)

