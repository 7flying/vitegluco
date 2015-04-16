# -*- coding: utf-8 -*-

def store_uuid(uuid, status='PENDING'):
    """Stores a uuid in the db with the specified status.
    
    :param uuid: uuid to store.
    :param status: status of the uuid, possible values are: PENDING, ACK, NACK.
    :exception ValueError: when wrong status is used.
    """
    if status != 'PENDING' or status != 'ACK' or status != 'NACK':
        raise ValueError('{status} wrong, use PENDING, ACK or NACK'.format(
            status=status))

def get_status(uuid):
    """Returns the status (PENDING, ACK, NACK) of the request specified by
    the uuid.

    :param uuid: uuid to check
    """
    pass

