
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Load data
books = pd.read_csv("Books.csv", encoding='latin-1')
users = pd.read_csv("Users.csv", encoding='latin-1')
ratings = pd.read_csv("Ratings.csv", encoding='latin-1')

# Data cleaning and transformation
books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]
books.rename(columns={'Book-Title': 'title', 'Book-Author': 'author', 'Year-Of-Publication': 'year', 'Publisher': 'publisher'}, inplace=True)

users.rename(columns={'User-ID': 'user_id', 'Location': 'location', 'Age': 'age'}, inplace=True)

ratings.rename(columns={'User-ID': 'user_id', 'Book-Rating': 'rating'}, inplace=True)

rated_200_books = ratings['user_id'].value_counts() > 200
book_geeks = rated_200_books[rated_200_books].index
ratings = ratings[ratings['user_id'].isin(book_geeks)]

# Merge data
books_with_ratings = ratings.merge(books, on="ISBN")

# Filtering and aggregation
num_rating = books_with_ratings.groupby('title')['rating'].count().reset_index()
num_rating.rename(columns={'rating': 'number of ratings'}, inplace=True)

final_rating_books = books_with_ratings.merge(num_rating, on='title')
final_rating_books = final_rating_books[final_rating_books['number of ratings'] >= 50]
final_rating_books.drop_duplicates(['user_id', 'title'], inplace=True)

# Pivot table
book_pivot = final_rating_books.pivot_table(columns='user_id', index='title', values='rating')
book_pivot.fillna(0, inplace=True)

# Sparse matrix
book_sparse = csr_matrix(book_pivot)

# Model training
model = NearestNeighbors(algorithm='brute')
model.fit(book_sparse)


# Recommendation function
def book_recommendation_system(book_name):
    if book_name not in book_pivot.index:
        print("Book '{}' not found in the dataset.".format(book_name))
        return

    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    # Print recommendations in a user-friendly format
    print("Recommendations based on '{}':".format(book_name))
    for i in range(1, len(suggestions[0])):
        recommended_book_id = suggestions[0][i]
        recommended_book_name = book_pivot.index[recommended_book_id]
        print("- {}".format(recommended_book_name))


# Example usage
book_to_recommend_from = "Animal Farm"
book_recommendation_system(book_to_recommend_from
