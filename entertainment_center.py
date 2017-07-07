import fresh_tomatoes
import media

movies = []
movies.append(media.Movie('Jumanji: Welcome to the Jungle',
                        'https://www.youtube.com/watch?v=2QKg5SZ_35I',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3NTQ0OTU0M15BMl5BanBnXkFtZTgwNTY4NTY3MjI@._V1._SX140_CR0,0,140,209_.jpg'))
movies.append(media.Movie('The Greatest Showman',
                        'https://www.youtube.com/watch?v=AXCTMGYUg9A',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyNzgzMzMwMV5BMl5BanBnXkFtZTgwNzMwNDU3MjI@._V1._SY209_CR0,0,140,209_.jpg'))
movies.append(media.Movie('Atomic Blonde',
                        'https://www.youtube.com/watch?v=yIUube1pSC0',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMjM5NDYzMzg5N15BMl5BanBnXkFtZTgwOTM2NDU1MjI@._V1._SX140_CR0,0,140,209_.jpg'))
movies.append(media.Movie('The Foreigner',
                        'https://www.youtube.com/watch?v=33iuQu3UtjI',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMjc0NzQ3OF5BMl5BanBnXkFtZTgwODMxMDM3MjI@._V1._SY209_CR0,0,140,209_.jpg'))
movies.append(media.Movie('Death Note',
                        'https://www.youtube.com/watch?v=gvxNaSIB_WI',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMzkxZmFmZDItMjNlMi00ZGQxLWEwMTQtNTlmMmZmMDMzOTA4XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1._SX140_CR0,0,140,209_.jpg'))
movies.append(media.Movie('Spider-Man: Homecoming',
                        'https://www.youtube.com/watch?v=U0D3AOldjMU',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1._SX140_CR0,0,140,209_.jpg'))

fresh_tomatoes.open_movies_page(movies)
