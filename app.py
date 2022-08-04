from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongodb+srv://codesejin:skl035512!@Cluster0.li6sx.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta_plus_week3


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/matjip', methods=["GET"])
def get_matjip():
    # 맛집 목록을 반환하는 API
    return jsonify({'result': 'success', 'matjip_list': []})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)