from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api_resources.wikipedia_resource import Wikipedia


app = Flask(__name__)



api = Api(app, prefix="/api")

cors = CORS(app, resources={r"/api/*":{"origins":"*"}})

api.add_resource(Wikipedia, "/wikipedia")

@app.route("/")
def index():
    return "Hello World"
if __name__ =="__main__":
    app.run()
