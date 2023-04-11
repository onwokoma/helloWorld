from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Olivia Nwokoma! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/favorite-course', methods=['GET', 'POST'])
def favorite_course():
    print('Subject entered: ' + request.args.get('subject_name'))
    print('Course number entered: ' + request.args.get('course_number'))
    more_courses = ['BMGT301', 'BMGT302', 'BMGT402', 'BMGT403']

    return render_template('favorite-course.html', courses=more_courses)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

@app.route('/restaurant-info')
def restaurant_info():  # put application's code here
   return render_template('restaurant-info.html')


@app.route('/restaurant-add', methods=['GET', 'POST'])
def restaurant_add():  # put application's code here
    if request.method == 'POST':
        return render_template('restaurant-add.html', form_submitted=True)
    else:
        return render_template('restaurant-add.html')

@app.route('/restaurant-delete', methods=['GET', 'POST'])
def restaurant_delete():  # put application's code here
    if request.method == 'POST':
        return render_template('restaurant-delete.html', form_submitted=True)
    else:
        return render_template('restaurant-delete.html')

if __name__ == '__main__':
    app.run()
