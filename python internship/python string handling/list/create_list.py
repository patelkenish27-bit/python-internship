movie=["the batman","avengers","spider man","thor regnarok","black panther"]
append_movie=input("Enter a movie name to add to the list: ")
movie.append(append_movie)
print("Updated movie list:\n", movie)
movie.remove(movie[0])
print("Updated movie list after removal:\n", movie)
