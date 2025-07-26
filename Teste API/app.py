from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'A Metamorfose',
        'autor': 'Franz Kafka',
    },
    {
        'id': 2,
        'titulo': 'O Arqueiro',
        'autor': 'Bernard Cornwell',
    },
    {       
        'id': 3,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien',
    },
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)  

# Rodar a aplicação
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
