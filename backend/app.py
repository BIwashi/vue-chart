from flask import Flask
from views import general
# from controller import ranking

app = Flask(__name__)
app.register_blueprint(general, url_prefix='/')
# app.register_blueprint(geo.app, url_prefix="/")
# app.register_blueprint(music.app, url_prefix="/")
# app.register_blueprint(ranking.app, url_prefix="/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)