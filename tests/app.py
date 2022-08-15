from __future__ import absolute_import
import web
import os
import sys

from webpy_graphql import GraphQLView
from .schema import Schema
import six


class index(GraphQLView):
    class GraphQLMeta:
        schema=Schema

def create_app(**kwargs):
    for key, value in six.iteritems(kwargs):
        setattr(index.GraphQLMeta, key, value)
    urls = ('/graphql', 'index')
    return web.application(urls, globals())


def is_test():
    if 'TEST_ENV' in os.environ:
        return os.environ['TEST_ENV'] == 'webpy-graphql'

if __name__ == "__main__":
    app = create_app(graphiql=True)
    app.run()
