from flask import Blueprint, request, abort, jsonify
import csv
import json
import glob
import re
import os


# Blueprintのオブジェクトを生成する
app = Blueprint('func', __name__)


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
    filepath = '../data/test001.csv'
    with open(filepath, 'r') as f:
        # list of dictの作成
        for line in csv.DictReader(f):
            json_list.append(line)

    json_data = jsonify(json_list)  # list型からjsonに変換
    return json_data
