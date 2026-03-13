
# Movie Recommendation System

This project is a **content-based movie recommendation system** built using Python and machine learning techniques.

The system recommends movies similar to a movie entered by the user.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Natural Language Processing

## How It Works
1. Movie metadata such as genres, keywords, cast, and overview are processed.
2. The text data is converted into vectors using CountVectorizer.
3. Cosine similarity is used to calculate similarity between movies.
4. The system recommends the most similar movies.

## Example

Input:
Avatar

Output:
Aliens  
Moonraker  
Alien  
Alien³  
Silent Running  

## Dataset

The dataset used is the **TMDB 5000 Movie Dataset**.

Download from:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Required files:
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

## Limitations
- The system only recommends movies present in the dataset.
- The dataset mainly contains **Hollywood movies**, so most recommendations are **English movies**.
- TV shows such as *Stranger Things* are not included.

## How to Run

Install required libraries:

pip install pandas scikit-learn numpy

Run the program:

python movie_recommender.py
