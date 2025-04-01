import streamlit as st
import json

# Load & save library data
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Initialize the library
library = load_library()
st.title("Personal Library Manager")

menu = st.sidebar.radio("Select an option", ["View Library", "Add Book", "Remove Book", "Search Book", "Save and Exit"])

if menu == "View Library":
    st.sidebar.header("Your Library")
    if library:
        st.table(library)
    else:
        st.write("Your library is empty. Add some books!")

elif menu == "Add Book":
    st.sidebar.header("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=2022, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Read this Book")

    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library()
        st.success("✔ Book Added Successfully!")
        st.rerun()

elif menu == "Remove Book":
    st.sidebar.header("Remove a Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        Selected_book = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != Selected_book]
            save_library()
            st.success("Book removed successfully!")
            st.rerun()
    else:
        st.warning("No books in your library. Add some books first!")

elif menu == "Search Book":
    st.sidebar.header("Search a Book")
    search_term = st.text_input("Enter title or author name")

    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No book found!")

elif menu == "Save and Exit":
    save_library()
    st.success("Your library has been successfully updated.")
