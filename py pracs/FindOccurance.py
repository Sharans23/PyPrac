import sqlite3
import re
from collections import Counter

def create_table():
    # Connect to SQLite database (or create one if it doesn't exist)
    conn = sqlite3.connect("word_counts.db")
    cursor = conn.cursor()

    # Create a table to store word counts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS word_counts (
            word TEXT PRIMARY KEY,
            count INTEGER
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

def process_data(file_path):
    # Read data from the file
    with open(file_path, 'r') as file:
        data = file.read()

    # Use regular expression to extract words
    words = re.findall(r'\b\w+\b', data)

    # Count occurrences of each word
    word_counts = Counter(words)

    # Store word counts in the database
    conn = sqlite3.connect("word_counts.db")
    cursor = conn.cursor()

    for word, count in word_counts.items():
        # Try to insert the word into the database; if it already exists, update the count
        cursor.execute("INSERT OR REPLACE INTO word_counts (word, count) VALUES (?, ?)", (word, count))

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "_main_":
    # Create the table if not exists
    create_table()

    # Process data from a file and store word counts in the database
    file_path = "sample_text.txt"  # Provide the path to your text file
    process_data(file_path)