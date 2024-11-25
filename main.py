from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Ömer'
    dersler = ['Matematik', 'Türkçe', 'Sosyal Bilgiler', 'Fizik', 'Kimya']
    return render_template("index.html", dersler=dersler, name=name)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

if __name__=="__main__":
    app.run(debug=True)
    
# Invalid Url    
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500