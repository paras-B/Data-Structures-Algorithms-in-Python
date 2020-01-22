"""Write a Python program that simulates a system that supports the functions
of an e-book reader. You should include methods for users of your
system to “buy” new books, view their list of purchased books, and read
their purchased books. Your system should use actual books, which have
expired copyrights and are available on the Internet, to populate your set
of available books for users of your system to “purchase” and read."""

import json
import pandas as pd

class BookApp:
    """I am taking a local json file to feed data in this simulation
        case, since this is just a simulation.
        modification, may be required when integrating with other db's
        in the backend.
    """
    def __init__(self, db="books.json", user_name="default",
                 user_email="default@email.com", shopping_cart=[],
                 purchased_item_cart=[]):
        self.db=db
        self.user_name = user_name
        self.user_email = user_email
        self.shopping_cart = shopping_cart
        self.purchased_item_cart = purchased_item_cart

    """The method list_of_books returns a smaller dataframe from json file
       we query only selected columns and return them to user.
       so, that they can select the books based on the index number.
    """
    def list_of_books(self):
        try:
            with open(self.db) as f:
                data = json.load(f)
                books_df = pd.DataFrame(data['books'], columns=['author', 'title'])
            f.close()
            return books_df
        except IOError:
            print("File/db not found.")

    """This method buy_books takes in id of each index and then
        we query the dataframe to get the row based on index.
        after providing the index as a parameter in the method, we save the resepctive
        row from the dataframe into user's cart.
    """
    def buy_books(self, id_book):
        with open(self.db) as f:
            data=json.load(f)
            detail_books_df = pd.DataFrame(data['books'])
        select_book = detail_books_df.iloc[id_book]
        self.shopping_cart.append(select_book)
        return self.shopping_cart

    """This method provides detail of the items that are in the user's cart """
    def view_cart(self):
        self.shopping_cart_df = pd.DataFrame(self.shopping_cart)
        return self.shopping_cart_df

    """This method purchased_items keeps records of books after purchasing and checkout
        from shopping cart. it will only contain purchased items
        user can input book id and make a purchase
    """
    def items_to_purchase(self, id_book):
        self.purchased_item_cart.append(self.view_cart().loc[id_book])
        return self.purchased_item_cart

    """This method lets the user to read the purchased book.
        if they have purchased multiple books and the books are in their
        purchased cart, then they have to provide the id of book they would
        like to read.
    """
    def read_purchased_books(self, id_book):
        self.purchased_item_cart_df = pd.DataFrame(self.purchased_item_cart)
        return self.purchased_item_cart_df.loc[id_book]


if __name__ == '__main__':
    new_app = BookApp()
    new_app.buy_books(4)
    new_app.buy_books(2)
    new_app.buy_books(5)
    print(new_app.view_cart())
    print(new_app.items_to_purchase(4))
    print(new_app.read_purchased_books(4))
