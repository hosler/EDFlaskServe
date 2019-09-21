from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

location = {}


class FSDJump(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("StarSystem", type=str)
        parser.add_argument("SystemSecurity_Localised", type=str)
        parser.add_argument("SystemSecondEconomy_Localised", type=str)
        parser.add_argument("FuelLevel", type=str)
        parser.add_argument("FuelUsed", type=str)
        parser.add_argument("SystemEconomy_Localised", type=str)
        parser.add_argument("timestamp", type=str)
        parser.add_argument("SystemSecondEconomy", type=str)
        parser.add_argument("SystemGovernment_Localised", type=str)
        parser.add_argument("SystemAllegiance", type=str)
        parser.add_argument("SystemEconomy", type=str)
        parser.add_argument("JumpDist", type=str)
        parser.add_argument("StarPos", type=str)
        parser.add_argument("SystemAddress", type=str)
        parser.add_argument("SystemSecurity", type=str)
        parser.add_argument("event", type=str)
        parser.add_argument("SystemGovernment", type=str)
        parser.add_argument("Population", type=str)
        global location
        args = parser.parse_args()
        location = args
        return {"data": args}


api.add_resource(FSDJump, '/FSDJump')

@app.route('/systeminfo')
def systeminfo():
    return render_template('FSDJump.html', system=location['StarSystem'], distance=location['JumpDist'])


if __name__ == '__main__':
    app.run(debug=True)
