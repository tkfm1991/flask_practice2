from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    fruits = {'1': 'もも', '2': 'りんご', '3': 'みかん'}
    # 値を受け取る
    # return render_template('result.html')
    fruit_no = request.args.get('fruit_no', '')
    try:
        return render_template('result.html', fruit=fruits[fruit_no])
    except KeyError:
        # KeyError発生時はインデックスへ遷移
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
