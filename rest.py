import os
from flask import Flask
from flask import request
from flask_restful import Resource, Api
import pyOceanus

app = Flask(__name__)
api = Api(app)

NLP_ENDPOINT = os.environ["NLP_ENDPOINT"]
try:
    oc = pyOceanus.Oceanus(NLP_ENDPOINT)
except ex:
    print(ex)
    exit()

class OceanusAPI(Resource):
    def post(self):
        intext = request.get_data().decode("UTF-8")
        od = oc.parse(intext)
        return {
            "tokens": od.tokens,
            "trees": [x.toJSON() for x in od.trees],
            "deps": od.deps
        }

api.add_resource(OceanusAPI, '/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
