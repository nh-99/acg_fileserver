from flask import Flask, request, send_from_directory
import requests
import os

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
auth_url = os.environ.get('ACG_AUTH_URL','bad')

@app.route('/files/<path:path>')
def send_file(path):
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    
    if username and password:
        r = requests.get(auth_url, params={'username':username, 'password':password})
        if r.json()["status"] == "success":
            return send_from_directory('files', path)
    
    return "{\"status\":\"error\"}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
