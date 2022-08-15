from __future__ import absolute_import
from graphql.type.definition import GraphQLArgument, GraphQLField, GraphQLNonNull, GraphQLObjectType
from graphql.type.scalars import GraphQLString, GraphQLInt
from graphql.type.schema import GraphQLSchema


def resolve_raises(*_):
    raise Exception("Throws!")


QueryRootType = GraphQLObjectType(
    name='QueryRoot',
    fields={
        'thrower': GraphQLField(GraphQLNonNull(GraphQLString), resolver=resolve_raises),
        'context': GraphQLField(
            GraphQLNonNull(GraphQLString),
            resolver=lambda self, info, **kwargs: info.context),

        'test': GraphQLField(
            GraphQLNonNull(GraphQLString),
            resolver=lambda self, info: 'Hello World'
        ),
        'test_args': GraphQLField(
            GraphQLNonNull(GraphQLString),
            args={'name': GraphQLArgument(GraphQLString)},
            resolver=lambda self, info, **kwargs: 'Hello {}'.format(kwargs.get("name"))
        ),
        'test_def_args': GraphQLField(
            GraphQLString,
            args={'name': GraphQLArgument(GraphQLString),},
            resolver=lambda self, info, name="World": 'Hello {}'.format(name)
        )
    }
)

MutationRootType = GraphQLObjectType(
    name='MutationRoot',
    fields={
        'writeTest': GraphQLField(
            QueryRootType,
            resolver=lambda *_: QueryRootType
        )
    }
)

Schema = GraphQLSchema(QueryRootType, MutationRootType)
