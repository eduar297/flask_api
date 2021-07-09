from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# @app.route("/person", methods=['POST', 'GET'])
# def handle_person():
#     if request.method == 'POST':
#         return "recived POST"
#     elif request.method == 'GET':
#         person1 = {"name": "Eduar2"}
#         resp = jsonify(person1)
#         # resp.status_code = 201
#         return resp, 200

# @app.route("/person", methods=['POST'])
# def create_person():
#     body = request.get_json()
#     if body is None:
#         return "The request body is null", 400
#     elif 'name' not in body:
#         return 'name required', 400
#     elif 'email' not in body:
#         return 'email required', 400
#     else:
#         return jsonify({"person":
#                         {"name": body["name"],
#                          "email": body["email"]
#                          }}), 200


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=4000, debug=True)
