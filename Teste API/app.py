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

@app.route('/livros')
def obter_livros():
    return jsonify(livros)

# Executar a aplicação
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
