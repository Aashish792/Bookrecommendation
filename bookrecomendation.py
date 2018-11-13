import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



books = pd.read_csv('books.csv', sep=';', error_bad_lines=False, encoding="latin-1")
books.columns = [ 'Title', 'Author', 'Genre', 'Height', 'Publisher']
users = pd.read_csv('Users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['UserId', 'Location', 'Age']
ratings = pd.read_csv('bookRating.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['Userid', 'bookRating']
