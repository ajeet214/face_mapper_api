from flask import Flask, request, jsonify
from raven.contrib.flask import Sentry
from modules.face_mapper import Mapper

app = Flask(__name__)

sentry = Sentry(app)


@app.route('/api/v1/face_mapper', methods=['POST', 'GET'])
def plus_mapper():
    global name, image, network
    if request.method == 'POST':
        request_data = request.get_json()
        name = request_data['full_name']
        image = request_data['image']
        network = request_data['network']

    obj = Mapper()
    res = obj.convertor(network, name, image)
    return jsonify({"data": res})


if __name__ == '__main__':
    app.run()
