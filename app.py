from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def restaurant_info():  # put application's code here
    return render_template('restaurant-info.html')

@app.route('/restaurant-add')
def restaurant_add():  # put application's code here
    return render_template('restaurant-add.html')

@app.route('/restaurant-delete')
def restaurant_delete():  # put application's code here
    return render_template('restaurant-delete.html')

if __name__ == '__main__':
    app.run()
