# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import abc


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
    def get_posts(self, imit=0):
        raise NotImplemented()

    @abc.abstractmethod
    def get_post_by_uid(self, uid=0):
        raise NotImplemented()

    @abc.abstractmethod
    def get_posts_timestamp_range(self, timestamp_start, timestamp_end):
        raise NotImplemented()

    @abc.abstractmethod
    def delete_post(self, post_id):
        raise NotImplemented()
