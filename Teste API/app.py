from flask import Flask, jsonify, request

app = flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'A Metamorfose',
        'autor': 'Franz Kafka',
    }
    {
        'id': 2,
        'titulo': 'O Arqueiro',
        'autor': ' Bernard Cornwell',
    },
    {       
         'id': 3,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien',
    },
]

 