#this is like the main method.
import media
import fresh_tomatoes

#def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
toy_story = media.Movie(
    "Toy Story", "A story of a boy and his toys that come to life",
    "https://1.bp.blogspot.com/-4CEJ24flM5U/T-ePLTwLdyI/AAAAAAAAHcQ/GGYVN8SVxG0/s1600/Toy+Story+%281995%29+1.jpg",
    "https://www.youtube.com/watch?v=Ny_hRfvsmU8"
)
#print(toy_story.storyline)

avatar = media.Movie(
    "Avatar", "A marine on an alien planet",
    "http://3.bp.blogspot.com/-f1__w3fEgVA/TvmWJIkT2xI/AAAAAAAAAEQ/VcRUr8_MU8Q/s1600/avatar-movie-desktop-wallpaper.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)
#print(avatar.storyline)
#avatar.show_trailer()

goal = media.Movie(
    "Goal the Dream Begins", "Story of a soccer player who gets a chance to play in Europe",
    "http://i.walmartimages.com/i/p/00/78/69/36/70/0078693670027_500X500.jpg",
    "https://www.youtube.com/watch?v=67LM5X9-MHA"
)
#print(goal.storyline)
#goal.show_trailer()

ratatouie = media.Movie(
    "Ratatouille", "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
)
movies = [toy_story, avatar, goal, ratatouie]
fresh_tomatoes.open_movies_page(movies)