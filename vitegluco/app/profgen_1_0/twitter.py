from flask import jsonify
from flask.ext.restful import Resource, reqparse
import uuid

from app import manager


class Twitter(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('uuid', type=str)
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('lastname', type=str, location='json')
        self.reqparse.add_argument('username', type=str, location='json')
        self.reqparse.add_argument('email', type=str, location='json')
        self.reqparse.add_argument('follow', type=list, location='json')
        self.reqparse.add_argument('mailauto', type=bool, default=False,
                                   location='json')
        self.reqparse.add_argument('mailtype', type=str, location='json')
        self.reqparse.add_argument('sex', type=str, location='json')
        self.reqparse.add_argument('bday', type=int, location='json')
        self.reqparse.add_argument('bday', type=int, location='json')
        self.reqparse.add_argument('bmonth', type=int, location='json') 
        self.reqparse.add_argument('byear', type=int, location='json')
        super(Twitter, self).__init__()

    def get(self):
        """Returns the status of the Twitter account creation request."""
        uid = self.reqparse.parse_args()['uuid']
        if uid is not None:
            status = manager.get_status(uid)
            return jsonify(uuid=uid, status=status)
        else:
            return jsonify(error="Must specify a UUID")
        
    
    def post(self):
        """Handles a POST to profgen/twitter, makes a request to create a
        Twitter account.
        """
        # TODO do something with this
        args = self.reqparse.parse_args()
        uid = uuid.uuid4()
        manager.store_uuid(uid)
        return jsonify(uuid=uid)
