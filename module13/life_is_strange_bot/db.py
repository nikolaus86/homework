import  sqlite3

from django.db import connection
from matplotlib.backend_bases import cursors

connection = sqlite3.connect("database.db")
cursor = connection.cursor()