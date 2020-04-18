from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Set username Set password
app.config['BASIC_AUTH_USERNAME'] = 'test'
app.config['BASIC_AUTH_PASSWORD'] = 'test@1234!'

# Setup Basic Authentication parameter.
secure_my_api = BasicAuth(app)

# Mock data test api
list_username = ['Noppong']

# Test apis
@app.route('/')
def hello():
    return 'Hello, World'


@app.route('/users', methods = ['POST'])
def create_user_profile():
    data = request.json
    # print(data)
    username = data["username"]

    # Check data in list_username
    check_has = username not in list_username
    if check_has:
        list_username.append(username)
        print(list_username)
        msg = "Success!"
    else:
        msg = "Fail!"

    # show the user profile for that user
    return jsonify(status = msg)


@app.route('/users', methods = ['GET'])
@secure_my_api.required
def show_all_username():
    return jsonify(all_users = list_username,
                   status = 200)


@app.route('/users/<username>', methods = ['GET'])
# @secure_my_api.required
def show_user_profile(username):
    msg = "Hello, {}"
    print("Input >>>", username)

    if username in list_username:
        fail_msg = msg.format(username)
        status = "Success"
        print(fail_msg)
    else:
        fail_msg = "Please, create username"
        status = "Fail"
        print("Please, create username")

    # show the user profile for that user
    return jsonify(messages = fail_msg,
        status = status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
