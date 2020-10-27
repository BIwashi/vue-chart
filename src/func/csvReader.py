from flask import Blueprint, request, abort, jsonify, request, redirect, url_for, url_for, send_from_directory, session
import csv
import json
import glob
import re
import os
import io
from datetime import datetime
import werkzeug
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '../data'
ALLOWED_EXTENSIONS = set(['csv'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SECRET_KEY'] = os.urandom(24)

# Blueprintのオブジェクトを生成する
app = Blueprint('func', __name__)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/csv')
def csvReader():
    # https://qiita.com/Amtkxa/items/1bc945bf434ae910a85f
    json_list = []
    json_data = {}
    print([os.path.basename(p) for p in glob.glob('../data/*.csv', recursive=True)
           if os.path.isfile(p)])
    '''
    現状はfilepathを変更して対応
    '''
    filepath = '../data/DATA020.CSV'
    with open(filepath, 'r') as f:
        # list of dictの作成
        for line in csv.DictReader(f):
            json_list.append(line)

    json_data = jsonify(json_list)  # list型からjsonに変換
    return json_data


@app.route("/getcsv", methods=["POST"])
def getcsv():
    if request.method == 'POST':
        send_data = request.files['send_data']
        if send_data and allowed_file(send_data.filename):
            filename = secure_filename(send_data.filename)
            send_data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            f = open('../data/' + filename, 'r')
            f_reader = csv.reader(f)
            result = list(f_reader)

    return "OK?"

    '''
    csv_data = {}
    csv_list = []

    filebuf = request.files['file']
    fileName = filebuf.filename
    filestring = filebuf.read()
    # csv_writer = csv.writer(filestring, delimiter=',', lineterminator='\n')
    f = csv.DictReader(filestring)
    csv_list.append(f)

    # csv_data = jsonify(csv_list)

    if filebuf is None:
        return jsonify(message='ファイルを指定してください'), 400
    elif 'text/csv' != filebuf.mimetype:
        return jsonify(message='CSVファイル以外は受け付けません'), 415

    # text_stream = io.TextIOWrapper(filebuf.stream, encoding='cp932')
    # for row in csv.reader(text_stream):
    #     # do something
    #     print(csv.reader(text_stream))
    print("--------------------")
    print(filebuf)
    print(fileName)
    # print(filestring)
    # print(filecsv)
    print(csv_list)
    print("--------------------")
    return "OK?"
'''
