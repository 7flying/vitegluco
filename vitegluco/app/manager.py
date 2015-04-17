# -*- coding: utf-8 -*-
from vitegluco import database

## UUIDS
UUID_KEY = 'uuid:'

## Emails
# Fields
E_EMAIL = 'email'
E_PASS = 'pass'
# Set of emails
EMAIL_SET_KEY = 'emails'
# Single email hash
EMAIL_KEY = 'email:'

## Bots
# Fields
B_EMAIL = 'email'
B_ACCOUNT = 'username'
B_CREATED_AT = 'created_at'
B_NAME = 'name'
B_LASTNAME = 'lastname'
B_SEX = 'sex'
B_BDATE = 'bdate'
B_PASS = 'pass'
# Set with Twitter, Facebook bot pks (email)
TWIBOT_SET_KEY = 'twitterbots'
FABOT_SET_KEY = 'facebookbots'
# Single bot hash
TWIBOT_KEY = 'twitterbot:'
FABOT_KEY = 'facebookbot:'


## ** uuid stuff ** ##
def store_uuid(uuid, status='PENDING'):
    """Stores a uuid in the db with the specified status.
    
    :param uuid: uuid to store.
    :param status: status of the uuid, possible values are: PENDING, ACK, NACK.
    :exception ValueError: when wrong status is used.
    """
    if status != 'PENDING' and status != 'ACK' and status != 'NACK':
        raise ValueError('{status} wrong, use PENDING, ACK or NACK'.format(
            status=status))
    else:
        database.set(UUID_KEY + str(uuid), status)

def get_status(uuid):
    """Returns the status (PENDING, ACK, NACK) of the request specified by
    the uuid.

    :param uuid: uuid to check
    """
    return database.get(UUID_KEY + str(uuid))
## ** end uuid stuff ** ##

## ** email stuff ** ##
def insert_email(email, password):
    email = str(email)
    password = str(password)
    if email not in database.smembers(EMAIL_SET_KEY):
        # Add hash
        database.hset(EMAIL_KEY + email, E_EMAIL, email)
        database.hset(EMAIL_KEY + email, E_PASS, password)
        # Add to set
        database.sadd(EMAIL_SET_KEY, email)
        return True
    else:
        return False

def get_pass_email(email):
    return database.hget(EMAIL_KEY + str(email), E_PASS)

def get_email_list():
    return database.smembers(EMAIL_SET_KEY)
## ** enf of email stuff ** ##

## ** bots stuff ** ##
def insert_bot(bottype, email, name, lastname, password, bdate=None, sex=None, \
               username=None):
    bottype = str(bottype)
    if bottype.upper() not in ('FACEBOOK', 'TWITTER'):
        return False
    if bottype.upper() == 'FACEBOOK':
        # Add hash
        database.hset(FABOT_KEY + email, B_NAME, name)
        database.hset(FABOT_KEY + email, B_LASTNAME, lastname)
        database.hset(FABOT_KEY + email, B_SEX, sex)
        database.hset(FABOT_KEY + email, B_EMAIL, email)
        database.hset(FABOT_KEY + email, B_PASS, password)
        database.hset(FABOT_KEY + email, B_BDATE, bdate)
        # Add to set
        database.sadd(FABOT_SET_KEY, email)
    else:
        # Add hash
        database.hset(TWIBOT_KEY + email, B_ACCOUNT, username)
        database.hset(TWIBOT_KEY + email, B_NAME, name)
        database.hset(TWIBOT_KEY + email, B_LASTNAME, lastname)
        database.hset(TWIBOT_KEY + email, B_EMAIL, email)
        database.hset(TWIBOT_KEY + email, B_PASS, password)
        # Add to set
        database.sadd(TWIBOT_SET_KEY, email)
    return True

def get_bot(email, bottype):
    """Returns a dict with the bot."""
    bottype = str(bottype)
    if bottype.upper() not in ('FACEBOOK', 'TWITTER'):
        return None
    if bottype.upper() == 'FACEBOOK':
        return database.hgetall(FABOT_KEY + email)
    else:
        return database.hgetall(TWIBOT_KEY + email)

def get_bots(bottype):
    """Returns a list of dicts holding bots."""
    bottype = str(bottype)
    if bottype.upper() not in ('FACEBOOK', 'TWITTER'):
        return None
    bots = database.smembers(TWIBOT_SET_KEY) if bottype.upper() == 'TWITTER' \
      else database.smembers(FABOT_SET_KEY)
    return [get_bot(x, bottype) for x in bots]
## ** end bots stuff ** ##
