# -*- coding: utf-8 -*-
from api_common import Gateway
from java_receiver import CaptchaSolver, DataReceiver


def generate_twitter(uuid, name, lastname, username, email, to_follow=None):
    """Generates a twitter account.
    :param uuid: unique identifier.
    :param name: person's name
    :param lastname: person's lastname
    :param username: requested Twitter username, if it is taken a random one
        will be selected.
    :param email: person's email.
    :param to_follow: list of accounts to follow.
    """
    data = DataReceiver()
    gateway = Gateway.generate_gateway()
    profgen = gateway.entry_point.getProfgen()
    if profgen is not None:
        profgen.generateTwitter(data, str(uuid), name, lastname, username,
                                email, to_follow)

def generate_twitter_email(uuid, name, lastname, username, email, email_type,\
                           sex, bday, bmonth, byear, to_follow=None):
    """Generates a Twitter account, generates the email on the fly on the
    selected email service (valid services are Gmail and Mailcom).

    :param uuid: unique identifier.
    :param name: person's name
    :param lastname: person's lastname
    :param username: requested Twitter username, if it is taken a random one
        will be selected.
    :param email: desired email.
    :param email_type: GMAIL or MAILCOM.
    :param sex: person's sex: m or f.
    :param bday: birth day.
    :param bmonth: birth month.
    :param byear: birth year.
    :param to_follow: list of accounts to follow.
    """
    data = DataReceiver()
    captcha = CaptchaSolver()
    gateway = Gateway.generate_gateway()
    profgen = gateway.entry_point.getProfgen()
    if profgen is not None:
        profgen.generateTwitterEmail(captcha, data, str(uuid), name, lastname,
                                     username, email, email_type.upper(),
                                     sex.lower(), bday, bmonth, byear, to_follow)
 
def generate_facebook(uuid, name, lastname, email, sex, bday, bmonth, byear,
                      friend_list=None):
    """Generates a Facebook account.
    :param uuid: unique identifier.
    :param name: person's name
    :param lastname: person's lastname
    :param email: email.
    :param sex: person's sex: m or f.
    :param bday: birth day.
    :param bmonth: birth month.
    :param byear: birth year.
    :param fiend_list: list of wanted friends.
    """
    data = DataReceiver()
    gateway = Gateway.generate_gateway()
    profgen = gateway.entry_point.getProfgen()
    if profgen is not None:
        profgen.generateFacebook(data, str(uuid), name, lastname, email,
                                 sex.lower(), bday, bmonth, byear, friend_list)

def generate_facebook_email(uuid, name, lastname, email, email_type, sex, bday,
                            bmonth, byear, friend_list):
    """Generates a Facebook account, generates the email on the fly on the
    selected email service (valid services are Gmail and Mailcom).

    :param uuid: unique identifier.
    :param name: person's name
    :param lastname: person's lastname
    :param email: desired email.
    :param email_type: GMAIL or MAILCOM.
    :param sex: person's sex: m or f.
    :param bday: birth day.
    :param bmonth: birth month.
    :param byear: birth year.
    :param fiend_list: list of wanted friends.
    """
    data = DataReceiver()
    gateway = Gateway.generate_gateway()
    profgen = gateway.entry_point.getProfgen()
    if profgen is not None:
        profgen.generateFacebookEmail(data, str(uuid), name, lastname, email,
                                      email_type.upper(), sex.lower(), bday,
                                      bmonth, byear, friend_list)
