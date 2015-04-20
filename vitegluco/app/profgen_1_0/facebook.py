from flask import jsonify
from flask.ext.restful import Resource, reqparse
import uuid
import threading

from app import manager
import generator
import api_common

class Facebook(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('uuid', type=str)
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('lastname', type=str, location='json')
        self.reqparse.add_argument('email', type=str, location='json')
        self.reqparse.add_argument('friends', type=list, location='json')
        self.reqparse.add_argument('mailauto', type=bool, default=False,
                                   location='json')
        self.reqparse.add_argument('mailtype', type=str, location='json')
        self.reqparse.add_argument('sex', type=str, location='json')
        self.reqparse.add_argument('bday', type=int, location='json')
        self.reqparse.add_argument('bday', type=int, location='json')
        self.reqparse.add_argument('bmonth', type=int, location='json') 
        self.reqparse.add_argument('byear', type=int, location='json')
        super(Facebook, self).__init__()
        
    def get(self):
        """Returns the status of the Facebook account creation request."""
        uid = self.reqparse.parse_args()['uuid']
        if uid is not None:
            status = manager.get_status(uid)
            return jsonify(uuid=uid, status=status)
        else:
            return jsonify(error="Must specify a UUID")

    def post(self):
        """Handles a POST to profgen/facebook, makes a request to create a
        Facebook account.
        """
        args = self.reqparse.parse_args()
        uid = uuid.uuid4()
        if args['name'] is not None and len(args['name']) > 0 and \
          args['lastname'] is not None and len(args['lastname']) > 0 and \
          args['sex'] is not None and args['sex'].upper() in ('M', 'F') and \
          args['email'] is not None and len(args['email']) > 0 and \
          args['bday'] > 0 and args['bmonth'] > 0 and args['byear'] > 1900:
          if not args['mailauto']:
              # Generate a simple Facebook account
              manager.store_uuid(uid)
              gen_thread = threading.Tread(target=generator.generate_facebook,
                                           args=(uid, args['name'],
                                                 args['lastname'],
                                                 args['email'], args['sex'],
                                                 args['bday'], args['bmonth'],
                                                 args['byear'],
                                                 args['friends']))
              gen_thread.start()
              return jsonify(uuid=uid, code=200)
          else:
              if args['mailtype'].upper() in api_common.EMAIL_SERVICES:
                  manager.store_uuid(uid)
                  gen_thread = threading.Tread(target=generator.generate_facebook,
                                               args=(uid, args['name'],
                                                     args['lastname'],
                                                     args['email'],
                                                     args['mailtype'],
                                                     args['sex'], args['bday'],
                                                     args['bmonth'],
                                                     args['byear'],
                                                     args['friends']))
                  gen_thread.start()
                  return jsonify(uuid=uid, code=200)
              else:
                  return jsonify(error="Incorrect params", code=400)
