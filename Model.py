from flask import Flask, request, jsonify, make_response
import json

from numpy import quantile

tasks = [
    {
        'id': 1,
        'name': "Lapis",
        "quantidade": 3
    },
    {
        "id": 2,
        "name": "Caneta",
        "quantidade": 10
    },
    {
        "id": 3,
        "name": "Borracha",
        "quantidade": 5
    }
]

tasksJSON = json.dumps(tasks)


class Model():
    def jsonReturn():
        return tasksJSON

    def soma():
        total = 0
        for x in tasks:
            total += x['quantidade']
        soma = str(total)
        return f'A quantidade total de produtos no estoque é de: {soma}'
