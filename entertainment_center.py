import media
import fresh_tomatos

toy_story = media.Movie("Toy Story","A story of a boy","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://youtu.be/KYz2wyBy3kc")

batman = media.Movie("Toy Story","A story of a boy","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://youtu.be/KYz2wyBy3kc")
# print(toy_story.storyline)

batmans = media.Movie("Toy Story","A story of a boy","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://youtu.be/KYz2wyBy3kc")
# print(toy_story.storyline)
# print(toy_story.storyline)

movies = [toy_story, batman, batmans]

fresh_tomatos.open_movies_page(movies)

