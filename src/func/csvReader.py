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

    with open('../data/testfile.csv', 'r') as f:
        # list of dictの作成
        for line in csv.DictReader(f):
            json_list.append(line)

    json_data = jsonify(json_list)  # list型からjsonに変換

    # print(json_data.key('time'))

    #     json_data["number"] = json_list

    # with open('../data/testfile.json', 'w') as f:
    #     # JSONへの書き込み
    #     json.dump(json_data, f)

    # print(json_list)
    # print(' ')
    # print(json_data)
    # time = [d.get('time') for d in json_data]

    # csv_file = open("../data/testfile.csv", "r",
    #                 encoding="ms932", errors="", newline="")
    # # リスト形式
    # fc = csv.reader(csv_file, delimiter=",", doublequote=True,
    #                 lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    # # 辞書形式
    # fj = csv.DictReader(csv_file, delimiter=",", doublequote=True,
    #                     lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    # for row in fj:
    #     # rowはdictionary
    #     # row["column_name"] or row.get("column_name")で必要な項目を取得することができる
    #     print(row)
    return json_data
