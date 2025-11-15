from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [
    {"label":"My first task", "done": False},
    {"label":"My second task", "done": False}
    ]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True) #convierte el JSON en diccionario para Python
    print("Incoming request with the following body",request_body)

    todos.append(request_body) #agrega el diccionario a la lista
    return jsonify(todos) #convierte la lista de Python a JSON

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        todos.pop(position)
    return jsonify(todos)
    print("this is position to delete:", position)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)