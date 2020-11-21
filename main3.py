from flask import Flask, render_template, request
app = Flask(__name__)
fruits = {'1': 'もも', '2': 'りんご', '3': 'みかん'}


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/result/<fruit_no>/')
def result(fruit_no):
    return render_template('result2.html', fruit=fruits[fruit_no], fruit_no=fruit_no)


@app.route('/output/<fruit_no>/')
def output(fruit_no):
    your_name = request.args.get('name', '')
    return render_template('output2.html', name=your_name, fruit=fruits[fruit_no])


if __name__ == '__main__':
    app.run(debug=True)
