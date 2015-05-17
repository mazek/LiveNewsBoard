# -*- coding: utf-8 -*-

import abc
from abc_base import PluginBase  # noqa


class Storage(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_db(self):
        raise NotImplemented()

    @abc.abstractmethod
    def put_post(self, timestamp, priority, sec_level,
                 author, source, message):
        raise NotImplemented()

    @abc.abstractmethod
    def get_messages(self, imit=0):
        raise NotImplemented()

    @abc.abstractmethod
    def get_message_by_id(self, id=0):
        raise NotImplemented()

    @abc.abstractmethod
    def get_messages_timestamp_range(self, timestamp_start, timestamp_end):
        raise NotImplemented()

    @abc.abstractmethod
    def delete_post(self, post_id):
        raise NotImplemented()
