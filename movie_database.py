import csv
import json
from urllib.request import urlopen

class Movie:
	def find_highest_rated(movie_file):
		
		movie_list = []

		with open(movie_file) as file:
			reader = csv.reader(file)

			for row in reader:
				if row:
					new_movie = Movie()
					new_movie.title = row[1]
					new_movie.imdb_rating = float(row[3])
					new_movie.director = row[2]
					movie_list.append(new_movie)

		highest_rated = movie_list[0]
		for movie in movie_list:
			if movie.imdb_rating > highest_rated.imdb_rating:
				highest_rated = movie

		return highest_rated

	

	def plot(self):
		webservice_url = "http://www.omdbapi.com/?i=tt0076759&plot=short&r=json"
		data = urlopen(webservice_url).read().decode("utf8")
# couldn't finish in time, needed to find a way to find search results for the correct movie
		result = json.loads(data)
		plot_summary = result['Plot']

		return plot_summary










