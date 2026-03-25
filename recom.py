# import libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer   # converts text into word counts
from sklearn.metrics.pairwise import cosine_similarity        # calculates similarity between books


# load datasets
books = pd.read_csv("archive/books.csv")          # main books dataset
book_tags = pd.read_csv("archive/book_tags.csv")  # mapping of books to tags
tags = pd.read_csv("archive/tags.csv")            # tag id to tag name mapping
 
# merge tag names into book_tags
book_tags = book_tags.merge(tags, on="tag_id")    # adds the tag_name column


# combine all tags of a book into one string
tag_strings = book_tags.groupby("goodreads_book_id")["tag_name"].apply(
    lambda x: " ".join(x)                          # joins tags like "fantasy magic adventure"
)


# merge the tag strings with the books dataset
books = books.merge(
    tag_strings,
    left_on="book_id",
    right_on="goodreads_book_id",
    how="left"
)


# keep only useful columns for recommendation
books = books[['book_id', 'title', 'average_rating', 'tag_name']]


# replace missing tag values with empty string
books['tag_name'] = books['tag_name'].fillna("")


# create a combined feature column (title + tags)
books['features'] = books['title'] + " " + books['tag_name']


# convert text into numerical vectors using Count Vectorizer
vectorizer = CountVectorizer(stop_words='english')

# create the count matrix
count_matrix = vectorizer.fit_transform(books['features'])


# calculate cosine similarity between all books
similarity = cosine_similarity(count_matrix)


# convert similarity matrix into dataframe for easier lookup
similarity_df = pd.DataFrame(
    similarity,
    index=books['title'],
    columns=books['title']
)

# recommendation function
def recommend_books(book_name):

    # get similarity scores of all books with the chosen book
    scores = similarity_df[book_name].sort_values(ascending=False)

    # remove the book itself from recommendations
    scores = scores.drop(book_name)

    # select top 10 similar books
    similar_books = scores.head(10).index

    # get those books from dataset
    recs = books[books['title'].isin(similar_books)]

    # sort them by rating
    recs = recs.sort_values(by='average_rating', ascending=False)

    print("\nTop 5 Similar Books:\n")
    

    # print top 5 recommendations
    for _, row in recs.head(5).iterrows():
        print(f"{row['title']} ⭐ {row['average_rating']}")

while True:

        # take user input
        user_input = input("\nFind books similar to: ").lower()

        # find matching books
        matches = books[books['title'].str.lower().str.contains(user_input)]

        # if no match found, restart loop
        if matches.empty:
            print("Book not found in dataset. Try again.\n")
            continue   # this skips everything below and restarts loop

        print("\nMatching books:\n")

        # show first 5 matches
        for i, title in enumerate(matches['title'].head(5)):
            print(f"{i+1}. {title}")

        # select first match (or you can upgrade this later)
        selected = matches.iloc[0]['title']
        print("\nUsing:", selected)

        # generate recommendations
        recommend_books(selected)

        # ask user if they want to continue
        choice = input("\nDo you want to search again? (y/n): ").lower()

        if choice != 'y':
            print("Goodbye")
            break