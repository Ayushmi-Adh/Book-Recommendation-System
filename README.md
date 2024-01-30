Certainly! Below is a README file template for your Book Recommendation System project:

![Alt Text](images/![librarian_gif_edited](https://github.com/Ayushmi-Adh/Book-Recommendation-System/assets/132826306/1706a070-706a-4eb4-b572-914186824c74)
)


---

# Book Recommendation System Project

This repository contains the code and queries for a Book Recommendation System project, aiming to provide personalized book suggestions based on user preferences and reading history.

## Table of Contents

1. [Introduction](#introduction)
2. [Queries](#queries)
    - [Data Loading and Cleaning](#data-loading-and-cleaning)
    - [User Filtering and Aggregation](#user-filtering-and-aggregation)
    - [Model Training and Recommendation Function](#model-training-and-recommendation-function)
3. [Usage](#usage)
4. [Explanation of Code](#explanation-of-code)
5. [Example Usage](#example-usage)
6. [Technologies Used](#technologies-used)
7. [License](#license)

## Introduction

The Book Recommendation System project is designed to help users discover new books based on their preferences and reading history. The system uses collaborative filtering techniques and a Nearest Neighbors algorithm for generating personalized recommendations.

## Queries

### Data Loading and Cleaning

1. **Loading and Cleaning Book Data:**
   - Loads book data from a CSV file, renames columns, and selects relevant features.
   ```python
   # Code 1
   import pandas as pd
   books = pd.read_csv("Books.csv", encoding='latin-1')
   books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]
   books.rename(columns={'Book-Title': 'title', 'Book-Author': 'author', 'Year-Of-Publication': 'year', 'Publisher': 'publisher'}, inplace=True)
   ```

2. **Loading and Cleaning User Data:**
   - Loads user data from a CSV file, renames columns.
   ```python
   # Code 2
   import pandas as pd
   users = pd.read_csv("Users.csv", encoding='latin-1')
   users.rename(columns={'User-ID': 'user_id', 'Location': 'location', 'Age': 'age'}, inplace=True)
   ```

3. **Loading and Cleaning Ratings Data:**
   - Loads ratings data from a CSV file, renames columns.
   ```python
   # Code 3
   import pandas as pd
   ratings = pd.read_csv("Ratings.csv", encoding='latin-1')
   ratings.rename(columns={'User-ID': 'user_id', 'Book-Rating': 'rating'}, inplace=True)
   ```

### User Filtering and Aggregation

4. **Filtering and Aggregating User Ratings:**
   - Filters out users with fewer than 200 ratings and aggregates ratings data.
   ```python
   # Code 4
   rated_200_books = ratings['user_id'].value_counts() > 200
   book_geeks = rated_200_books[rated_200_books].index
   ratings = ratings[ratings['user_id'].isin(book_geeks)]
   ```

5. **Pivot Table Creation and Sparse Matrix:**
   - Creates a pivot table and converts it to a sparse matrix for efficient processing.
   ```python
   # Code 5
   book_pivot = final_rating_books.pivot_table(columns='user_id', index='title', values='rating')
   book_pivot.fillna(0, inplace=True)
   book_sparse = csr_matrix(book_pivot)
   ```

### Model Training and Recommendation Function

6. **Model Training with Nearest Neighbors Algorithm:**
   - Trains a recommendation model using the Nearest Neighbors algorithm.
   ```python
   # Code 6
   model = NearestNeighbors(algorithm='brute')
   model.fit(book_sparse)
   ```

7. **Book Recommendation Function:**
   - Implements a function for book recommendations based on user input.
   ```python
   # Code 7
   def book_recommendation_system(book_name):
       # Function code
   ```

## Usage

To use this Book Recommendation System, follow these steps:

1. Ensure you have the necessary Python libraries installed, such as NumPy, Pandas, SciPy, and Scikit-learn.
2. Load the book, user, and ratings data into your Python environment.
3. Execute the provided code snippets sequentially.
4. Utilize the `book_recommendation_system` function for personalized book recommendations.

## Explanation of Code

Each code snippet is commented for clarity, explaining its purpose and the logic behind it. The code covers data loading, cleaning, user filtering, aggregation, model training, and the recommendation function.

## Example Usage

Here is an example of how to use the Book Recommendation System:

```python
# Example Usage
book_to_recommend_from = "Animal Farm"
book_recommendation_system(book_to_recommend_from)
```

## Technologies Used

The project is implemented in Python, utilizing libraries such as NumPy, Pandas, SciPy, and Scikit-learn for data manipulation, analysis, and model training.

## License

This project is licensed under the [MIT License](LICENSE).


