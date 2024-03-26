import streamlit as st
import psycopg2
import pandas as pd
  
def fetch_data():
    con=psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="postgresdb"   
    )
    query = "SELECT * FROM books"
    df = pd.read_sql(query, con=con)
    con.close() 
    return df


def insert_data(title, auther, id):
    con = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="postgresdb"   
    )
    cur = con.cursor()
    query = "INSERT INTO books (title, auther, id) VALUES (%s, %s, %s)"
    cur.execute(query, (title, auther, id))
    con.commit()
    con.close()


def delete_data(book_id):
    con = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="postgresdb"   
    )
    cur = con.cursor()
    query = "DELETE FROM books WHERE id = %s"
    cur.execute(query, (book_id,))
    con.commit()
    con.close()


def update_data(book_id, new_title, new_author):
    con = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="postgresdb"   
    )
    cur = con.cursor()
    query = "UPDATE books SET title = %s, auther = %s WHERE id = %s"
    cur.execute(query, (new_title, new_author, book_id))
    con.commit()
    con.close()


def main():
    st.set_page_config(page_title="May's books store", layout="wide")

    st.subheader("hi, Im May :wave:")
    st.title("Bookseller since 1999")
    st.write("love books")

    st.sidebar.subheader("Manage Books")
    selected_option = st.sidebar.radio("Select Action", ("Add a Book", "Delete a Book", "Update a Book"))

    if selected_option == "Add a Book":
            st.sidebar.subheader("Add a Book")
            title = st.sidebar.text_input("Title:")
            author = st.sidebar.text_input("Author:")
            id = st.sidebar.number_input("id:", min_value=0)
            if st.sidebar.button("Add Book"):
                insert_data(title, author, id)
                st.sidebar.success("Book added successfully!")


    elif selected_option == "Delete a Book":
        st.sidebar.subheader("Delete a Book")
        df = fetch_data()
        book_id_to_delete = st.sidebar.selectbox("Select Book to Delete", df["id"].tolist())
        if st.sidebar.button("Delete Book"):
            delete_data(book_id_to_delete)
            st.sidebar.success("Book deleted successfully!")

    elif selected_option == "Update a Book":
        st.sidebar.subheader("Update a Book")
        df = fetch_data()
        book_id_to_update = st.sidebar.selectbox("Select Book to Update", df["id"].tolist())
        new_title = st.sidebar.text_input("Enter new title:")
        new_author = st.sidebar.text_input("Enter new author:")
        if st.sidebar.button("Update Book"):
            update_data(book_id_to_update, new_title, new_author)
            st.sidebar.success("Book updated successfully!")

    st.subheader("Books Information")
    df = fetch_data()
    if not df.empty:
        st.write("Books Data:")
        st.write(df)
    else:
        st.write("No books found in the database.")
    

if __name__ == "__main__":
    main()