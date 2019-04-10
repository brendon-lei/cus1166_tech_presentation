import boto3
from flask import Flask, jsonify, render_template

app = Flask(__name__)
# Initialize dynamodb access
dynamodb = boto3.resource('dynamodb')
db = dynamodb.Table('myservice-dev')

@app.route('/pic')
def picture():
    return render_template('pic.html')

@app.route('/counter', methods=['GET'])
def counter_get():
  res = db.get_item(Key={'id': 'counter'})
  return jsonify({'counter': res['Item']['counter_value']})

@app.route('/counter/increase', methods=['POST'])
def counter_increase():
  res = db.get_item(Key={'id': 'counter'})
  value = res['Item']['counter_value'] + 1
  res = db.update_item(
    Key={'id': 'counter'},
    UpdateExpression='set counter_value=:value',
    ExpressionAttributeValues={':value': value},
  )
  return jsonify({'counter': value})