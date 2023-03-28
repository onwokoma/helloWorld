from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Olivia Nwokoma! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/favorite-course')
def favorite_course():  # put application's code here
    print('Subject entered: ' + request.args.get('subject_name'))
    print('Course number entered: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('First name entered: ' + request.form.get('first_name'))
        print('Last name entered: ' + request.form.get('last_name'))
        print('Email entered: ' + request.form.get('email'))

        # used to check if the checkbox was checked. need this or else the field is not passed back.
        if request.form.get('agree_check'):
            print('Agree to be contacted entered: ' + request.form.get('agree_check'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
