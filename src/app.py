from flask import request
from flask import Flask, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():

    json_text = jsonify(todos)
    return todos


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body",request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        del todos[position] 
    except IndexError:
        return jsonify({"error": "Posición no válida"}), 404
    return jsonify(todos) 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)