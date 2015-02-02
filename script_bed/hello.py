from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route('/pingme')
def hello_world():
  return 'Hello world!'

@app.route('/payload', methods = ['POST'])
def receive_web_hook():
  json_data = request.get_json(force=TRUE)
  myscript = "/home/will/william-elder.com/public/.git/hooks/post-receive"
  process = subprocess.call(myscript)
  return process

if __name__ == '__main__':
  app.run()
