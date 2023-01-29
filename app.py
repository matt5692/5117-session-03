from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/hi', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

# global entries list
entries = []

@app.get('/apologyForm')
def process_entry():
  entries.append(request.args.get("name", "unknown"))
  return render_template('index.html', entry_list=entries)

  