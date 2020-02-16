import os
from gql import gql, Client as gql_client
from gql.transport.requests import RequestsHTTPTransport


HOST = os.environ.get('LAZY_APP_HOST', 'backend')
PORT = os.environ.get('LAZY_APP_PORT', '5000')


client = gql_client(
    transport=RequestsHTTPTransport(
            url=f'http://{HOST}:{PORT}/graphql',
            use_json=True
        ),
    fetch_schema_from_transport=True,
)

CREATE_MOVIE_MUTATION = gql("""
    mutation CreateMovie($name: String! $year: Int){
        createMovie(name:$name, year: $year){
            movie{id name}
        }
    }
""")

GET_MOVIES_QUERY = gql("""
    query GetMovies{
            movies {
                id
                name
                year
                torrent{id}
            }
        }
""")