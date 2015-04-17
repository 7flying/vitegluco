# -*- coding: utf-8 -*-

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
    pass

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
    :param sex: person's sex: M or F.
    :param bday: birth day.
    :param bmonth: birth month.
    :param byear: birth year.
    :param to_follow: list of accounts to follow.
    """
    pass
