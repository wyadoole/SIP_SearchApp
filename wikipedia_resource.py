from flask_restful import Resource, reqparse, abort
import wikipediaapi

class Wikipedia(Resource):
    def __init__(self):
        # http://my.app/api/wikipedia?search=dolphins
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('search', type=str, required=True, help="The search term", location=['args'])

        #init
        super().__init__()

    def get(self):
        # parse out the arguments
        args = self.parser.parse_args()

        wiki =wikipediaapi.Wikipedia("en")
        result = wiki.page(args["search"])

        if not result.exists():
            abort(404)

        return result.summary, 200



