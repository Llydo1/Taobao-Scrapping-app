import tkinter as tk
import pymongo


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("MongoDB Browser")

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.databases = self.client.list_database_names()

        # Create the widgets
        self.select_db_label = tk.Label(self.master, text="Select a database:")
        self.select_db_label.pack(pady=10)
        self.db_var = tk.StringVar(value=self.databases)
        self.db_listbox = tk.Listbox(self.master, listvariable=self.db_var, height=10)
        self.db_listbox.pack()
        self.list_collections_button = tk.Button(self.master, text="List collections", command=self.list_collections)
        self.list_collections_button.pack(pady=10)
        self.collections_label = tk.Label(self.master, text="")
        self.collections_label.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(pady=10)

    def list_collections(self):
        # Get the selected database
        selected_db = self.db_listbox.get(self.db_listbox.curselection())

        # Get the collections in the database
        collections = self.client[selected_db].list_collection_names()

        # Update the collections label
        self.collections_label.config(text=f"Collections in {selected_db}:\n{', '.join(collections)}")


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
