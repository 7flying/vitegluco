from flask import jsonify
from flask.ext.restful import Resource, reqparse
import uuid

from app import manager
import api_common

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
        # TODO call generator's methods
        args = self.reqparse.parse_args()
        # Generate uuid
        uid = uuid.uuid4()
        if args['name'] is not None and len(args['name']) > 0 and \
          args['lastname'] is not None and len(args['lastname']) > 0 and \
          args['username'] is not None and len(args['username']) > 0 and \
          len(args['username']) < 16 and args['email'] is not None and \
          len(args['email']) > 0:
          if not args['mailauto']:
              # Generate a simple twitter account
              manager.store_uuid(uid)
              return jsonify(uuid=uid, code=200)
          else:
              if args['sex'] is not None and args['sex'].upper() in ('M', 'F')\
                and args['mailtype'] is not None and \
                (args['mailtype'].upper() in api_common.EMAIL_SERVICES) and \
                args['bday'] > 0 and args['bmonth'] > 0 and args['byear'] > 1900:
                  # Generate an email account on the fly
                  manager.store_uuid(uid)
                  return jsonify(uuid=uid, code=200)
              else:
                  return jsonify(error="Incorrect params", code=400)
        else:
            return jsonify(error="Incorrect params", code=400)
