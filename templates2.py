from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/index/<user>')
def index_page(user):
    return render_template('greet.html',name=user)


@app.route('/grading/<int:score>')
def grading_page(score):
    return render_template('grades.html',mark=score)

@app.route('/register/')
def register():
    names = {'Chelsea':'Laguma','Odwa':'Nodada','Zoe':'Engel'}
    return render_template('myregister.html',register=names)



if __name__=='__main__':
    app.run(debug=True)
