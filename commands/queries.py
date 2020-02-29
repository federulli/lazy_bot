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

CREATE_TV_SHOW_MUTATION = gql("""
    mutation CreateTVShow($name: String!){
        createTvShow(name:$name){
            tvShow{id}
        }
    }
""")

GET_TV_SHOWS_QUERY =  gql("""
    query GetTvShows {
            tvShows{
            id
            name
            }
        }
""")

CREATE_SEASON_MUTATION =  gql("""
    mutation CreateSeason($show_id: ID! $number: Int!){
        createSeason(tvShowId:$show_id, number: $number){
            season{number}
        }
    }
""")

LIST_SEASONS_QUERY = gql("""
    query GetSeason($tv_show_id: ID!) {
        seasons(tvShowId: $tv_show_id){
            id
            chapters{number}
            completed
            number
            chapterCount
        }
    }
""")