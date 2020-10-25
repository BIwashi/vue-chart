from flask import Flask, render_template
from func import csvReader

app = Flask(__name__)
# 分割したblueprintを登録する
app.register_blueprint(csvReader.app, url_prefix='/api')


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
