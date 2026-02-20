import requests

def get_movie_info_by_name(movie_name):
    url = f'https://moviesapi.ir/api/v1/movies'

    parameter = {
        'q' : movie_name
    }
    response = requests.get(url, params=parameter)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        data = response['data'][0]
        title = data['title']
        year = data['year']
        country = data['country']
        imdb_rate = data['imdb_rating']
        genres = data['genres']
        return (title, year, country, imdb_rate, genres)
    

if __name__ == '__main__':
    movie_name = input('Enter movie name: ')
    result = get_movie_info_by_name(movie_name)
    print(result)         