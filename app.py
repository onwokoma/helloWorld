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

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Student, Major
from datetime import datetime as dt

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'university.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'beyond_course_scope'
db.init_app(app)


@app.route('/student/view')
def student_view_all():
    students = Student.query.outerjoin(Major, Student.major_id == Major.major_id) \
        .add_entity(Major) \
        .order_by(Student.last_name, Student.first_name) \
        .all()
    return render_template('student_view_all.html', students=students)


@app.route('/student/view/<int:student_id>')
def student_view(student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    majors = Major.query.order_by(Major.major) \
        .order_by(Major.major) \
        .all()

    if student:
        return render_template('student_entry.html', student=student, majors=majors, action='read')

    else:
        flash(f'Student attempting to be viewed could not be found!', 'error')
        return redirect(url_for('student_view_all'))

@app.route('/student/create', methods=['GET', 'POST'])
def student_create():
    if request.method == 'GET':
        majors = Major.query.order_by(Major.major) \
            .order_by(Major.major) \
            .all()
        return render_template('student_entry.html', majors=majors, action='create')
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        major_id = request.form['major_id']

        birth_date = request.form['birth_date']
        is_honors = True if 'is_honors' in request.form else False

        student = Student(first_name=first_name, last_name=last_name, major_id=major_id,
                          birth_date=dt.strptime(birth_date, '%Y-%m-%d'), is_honors=is_honors)
        db.session.add(student)
        db.session.commit()
        flash(f'{first_name} {last_name} was successfully added!', 'success')
        return redirect(url_for('student_view_all'))

    flash('Invalid action. Please try again.', 'error')
    return redirect(url_for('student_view_all'))


@app.route('/student/update/<int:student_id>', methods=['GET', 'POST'])
def student_edit(student_id):
    if request.method == 'GET':
        student = Student.query.filter_by(student_id=student_id).first()
        majors = Major.query.order_by(Major.major) \
            .order_by(Major.major) \
            .all()

        if student:
            return render_template('student_entry.html', student=student, majors=majors, action='update')

        else:
            flash(f'Student attempting to be edited could not be found!', 'error')

    elif request.method == 'POST':
        student = Student.query.filter_by(student_id=student_id).first()

        if student:
            student.first_name = request.form['first_name']
            student.last_name = request.form['last_name']
            student.major_id = request.form['major_id']
            student.birthdate = dt.strptime(request.form['birth_date'], '%Y-%m-%d')
            student.num_credits_completed = request.form['num_credits_completed']
            student.gpa = request.form['gpa']
            student.is_honors = True if 'is_honors' in request.form else False

            db.session.commit()
            flash(f'{student.first_name} {student.last_name} was successfully updated!', 'success')
        else:
            flash(f'Student attempting to be edited could not be found!', 'error')

        return redirect(url_for('student_view_all'))

    return redirect(url_for('student_view_all'))

@app.route('/student/delete/<int:student_id>')
def student_delete(student_id):
    student = Student.query.filter_by(student_id=student_id).first()

    if student:
        db.session.delete(student)
        db.session.commit()
        flash(f'{student} was successfully deleted!', 'success')
    else:
        flash(f'Delete failed! Student could not be found.', 'error')

    return redirect(url_for('student_view_all'))


@app.route('/')
def home():
    return redirect(url_for('student_view_all'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Execute only once! Initial loading of available majors

        majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
                    'Operations Management & Business Analytics', 'Supply Chain Management']
        for each_major in majors:
            print(each_major)
            amajor = Major(major=each_major)
            db.session.add(amajor)
            db.session.commit()

    app.run()