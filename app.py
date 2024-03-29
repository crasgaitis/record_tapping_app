from flask import Flask, render_template, request
from datetime import datetime
import csv

app = Flask(__name__)

dots = [
    {"id": 1, "color": "blue"},
    {"id": 2, "color": "blue"},
    {"id": 3, "color": "blue"}
]

@app.route('/')
def index():
    return render_template('index.html', dots=dots)

@app.route('/record_click', methods=['POST'])
def record_click():
    dot_id = int(request.form['dot_id'])
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    record_event(timestamp, dot_id)
    return '', 204

def record_event(timestamp, dot_id):
    with open('click_events.csv', mode='a', newline='') as file:
        fieldnames = ['timestamp', 'clicked_item']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'timestamp': timestamp, 'clicked_item': dot_id})

if __name__ == '__main__':
    app.run(debug=True)
