from flask import jsonify


def bad_request(error):
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': 'Bad request',
            'error': error,
            'code': 400
        }
    )


def not_found():
    return jsonify(
        {
            'success': False,
            'data': {},
            'message': 'Resource not found',
            'code': 404
        }
    ), 404


def response(data):
    return jsonify(
        {
            'success': True,
            'data': data,
            'code': 200
        }
    ), 200
