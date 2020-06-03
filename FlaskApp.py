from flask import Flask, jsonify, request
import tensorflow as tf
import tensorflow_hub as hub
import sys
import logging
from healthcheck import HealthCheck

app = Flask(__name__)
logging.basicConfig(filename="flask.log", level=logging.DEBUG,
	                format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")
def howami():
    return True, "I am good"

health = HealthCheck(app, "/hcheck")
health.add_check(howami)

embed = hub.load("/app/useModel")

@app.route('/getvector',  methods=['POST'])
def getvector():
    searchString = request.args.get('searchString')  or request.get_json().get('searchString', '')
    embeddings = embed(searchString)
    searchVect = embeddings.numpy().tolist()
    for idx, vect in enumerate(searchVect):
        app.logger.info(f"Vector is calculated for string: \"{searchString[idx]}\" and is of dimension: {len(searchVect[idx])}")
    #print(searchVect, file=sys.stderr)
    return jsonify(searchVect)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2222, debug=True)