from tkinter import *
from tkinter import ttk
import ast

# Search by name year
# Add by attributes in the constructor
# Update by name year attribute value
# delete by name year

# should close the program and reopen it to save changes


with open('movies.txt', 'r') as movies_:
    dict1 = movies_.read()
    mov_dict = ast.literal_eval(dict1)

with open('books.txt', 'r') as books_:
    dict2 = books_.read()
    bk_dict = ast.literal_eval(dict2)

with open('computer_games.txt', 'r') as games_:
    dict3 = games_.read()
    gm_dict = ast.literal_eval(dict3)


class Movies:
    movie_dict = mov_dict

    def add_movie(self, title, year, director, length, genre, budget, rating):
        Movies.movie_dict[(title, year)] = {
            'director': director,
            'length': length,
            'genre': [_ for _ in genre],
            'budget': budget,
            'rating': rating}

    def delete_movie(self, movie, year):
        Movies.movie_dict.pop((movie, year))

    def view_movie_details(self, movie, year):
        return Movies.movie_dict[(movie, year)]

    def view_movie_director(self, movie, year):
        return Movies.movie_dict[(movie, year)]['director']

    def view_highest_rating(self):
        highest_rating = 0
        highest_movie = ''
        for movie in Movies.movie_dict:
            if Movies.movie_dict[movie]['rating'] > highest_rating:
                highest_rating = Movies.movie_dict[movie]['rating']
                highest_movie = movie[0]

        return f"Movie with the highest rating -> {highest_movie}, {highest_rating}"


class Books:
    books_dict = bk_dict

    def add_book(self, title, year, writer, length, genre, rating):
        Books.books_dict[(title, year)] = {
            'writer': writer,
            'length': length,
            'genre': [_ for _ in genre],
            'rating': rating}

    def delete_book(self, book, year):
        Books.books_dict.pop((book, year))

    def view_book_details(self, book, year):
        return Books.books_dict[(book, year)]

    def view_book_writer(self, book, year):
        return Books.books_dict[(movie, year)]['writer']

    def view_highest_rating(self):
        highest_rating = 0
        highest_book = ''
        for book in Books.books_dict:
            if Books.books_dict[book]['rating'] > highest_rating:
                highest_rating = Books.books_dict[book]['rating']
                highest_movie = book[0]

        return f"Movie with the highest rating -> {highest_book}, {highest_rating}"


class ComputerGames:
    games_dict = gm_dict

    def add_game(self, name, year, publisher, genre, mode, rating):
        ComputerGames.games_dict[(name, year)] = {
            'publisher': publisher,
            'genre': [_ for _ in genre],
            'mode': mode,
            'rating': rating}

    def delete_game(self, game, year):
        ComputerGames.games_dict.pop((game, year))

    def view_game_details(self, game, year):
        return ComputerGames.games_dict[(game, year)]

    def view_game_publisher(self, game, year):
        return ComputerGames.games_dict[(movie, year)]['publisher']

    def view_highest_rating(self):
        highest_rating = 0
        highest_game = ''
        for game in ComputerGames.games_dict:
            if ComputerGames.games_dict[game]['rating'] > highest_rating:
                highest_rating = ComputerGames.games_dict[game]['rating']
                highest_game = game[0]

        return f"Game with the highest rating -> {highest_game}, {highest_rating}"


# Visual
def select_option(option):
    def get_pair():
        searched_pair = text_entry.get().split()
        if option == 'Movies':
            try:
                name = ' '.join(searched_pair[:-1])
                year = int(searched_pair[-1])
                data = Movies.movie_dict[(name, year)]
                director_info.config(text=f"Director: {data['director']}")
                length_info.config(text=f"Length: {data['length']} min")
                genre_info.config(text=f"Genre: {', '.join(data['genre'])}")
                budget_info.config(text=f"Budget: {data['budget']}$")
                rating_info.config(text=f"Rating: {data['rating']} *")
                error.config(text='')
            except (IndexError, KeyError) as e:
                error.config(text='Movie is not available')

        elif option == 'Games':
            try:
                name = ' '.join(searched_pair[:-1])
                year = int(searched_pair[-1])
                data = ComputerGames.games_dict[(name, year)]
                publisher_info.config(text=f"Publisher: {data['publisher']}")
                mode_info.config(text=f"Mode: {data['mode']}")
                genre1_info.config(text=f"Genre: {', '.join(data['genre'])}")
                rating1_info.config(text=f"Rating: {data['rating']} *")
                empty.config(text="")
                error.config(text='')
            except (IndexError, KeyError) as e:
                error.config(text='Game is not available')

        elif option == 'Books':
            try:
                name = ' '.join(searched_pair[:-1])
                year = int(searched_pair[-1])
                data = Books.books_dict[(name, year)]
                writer_info.config(text=f"Writer: {data['writer']}")
                length_info.config(text=f"Length: {data['length']} pages")
                genre_info.config(text=f"Genre: {', '.join(data['genre'])}")
                rating_info.config(text=f"Rating: {data['rating']} *")
                error.config(text='')
            except (IndexError, KeyError) as e:
                error.config(text='Book is not available')

    def delete_pair():
        searched_pair = text_entry.get().split()
        if option == 'Movies':
            name = ' '.join(searched_pair[:-1])
            year = int(searched_pair[-1])
            Movies.delete_movie(Movies, name, year)

        elif option == 'Games':
            name = ' '.join(searched_pair[:-1])
            year = int(searched_pair[-1])
            ComputerGames.delete_game(ComputerGames, name, year)

        elif option == 'Books':
            name = ' '.join(searched_pair[:-1])
            year = int(searched_pair[-1])
            Books.delete_book(Books, name, year)

    def add_pair():
        added_pair = text_entry.get().split()

        if option == 'Movies':
            rating = added_pair[-1]
            budget = added_pair[-2]
            genre = [added_pair[-3]]
            length = added_pair[-4]
            director = ' '.join(added_pair[-6:-4])
            year = int(added_pair[-7])
            title = ''.join(added_pair[:-7])
            Movies.add_movie(Movies, title, year, director, length, genre, budget, rating)


        elif option == 'Games':
            rating = added_pair[-1]
            mode = added_pair[-2]
            genre = [added_pair[-3]]
            publisher = added_pair[-4]
            year = int(added_pair[-5])
            name = ' '.join(added_pair[:-5])
            ComputerGames.add_game(ComputerGames, name, year, publisher, genre, mode, rating)

        elif option == 'Books':
            rating = added_pair[-1]
            genre = [added_pair[-2]]
            length = added_pair[-3]
            writer = ' '.join(added_pair[-5: -3])
            year = int(added_pair[-6])
            title = ' '.join(added_pair[:-6])
            Books.add_book(Books, title, year, writer, length, genre, rating)

    def update_pair():
        selected_pair = text_entry.get().split()
        if option == 'Movies':
            value = selected_pair[-1]
            info_to_update = selected_pair[-2]
            year = int(selected_pair[-3])
            name = ' '.join(selected_pair[:-3])
            if info_to_update == 'genre':
                Movies.movie_dict[(name, year)][info_to_update] = [value]
            else:
                Movies.movie_dict[(name, year)][info_to_update] = value

        elif option == 'Games':
            value = selected_pair[-1]
            info_to_update = selected_pair[-2]
            year = int(selected_pair[-3])
            name = ' '.join(selected_pair[:-3])
            if info_to_update == 'genre':
                ComputerGames.games_dict[(name, year)][info_to_update] = [value]
            else:
                ComputerGames.games_dict[(name, year)][info_to_update] = value

        elif option == 'Books':
            value = selected_pair[-1]
            info_to_update = selected_pair[-2]
            year = int(selected_pair[-3])
            name = ' '.join(selected_pair[:-3])
            if info_to_update == 'genre':
                Books.books_dict[(name, year)][info_to_update] = [value]
            else:
                Books.books_dict[(name, year)][info_to_update] = value

    if option == 'Movies':
        text_entry = ttk.Entry(mainframe)
        text_entry.grid(row=4, column=0, columnspan=4, sticky='we')

        search_button = ttk.Button(mainframe, text='SEARCH...', command=get_pair)
        search_button.grid(row=5, column=0, sticky='we')

        add_button = ttk.Button(mainframe, text='ADD', command=add_pair)
        add_button.grid(row=5, column=1, sticky='we')

        delete_button = ttk.Button(mainframe, text='DELETE', command=delete_pair)
        delete_button.grid(row=5, column=2, sticky='we')

        update_button = ttk.Button(mainframe, text='UPDATE', command=update_pair)
        update_button.grid(row=5, column=3, sticky='we')

        director_info = Label(mainframe, text='Director: ')
        director_info.grid(row=6, column=0, sticky='we')

        length_info = Label(mainframe, text='Length: ')
        length_info.grid(row=7, column=0, sticky='we')

        genre_info = Label(mainframe, text='Genre: ')
        genre_info.grid(row=8, column=0, sticky='we')

        budget_info = Label(mainframe, text='Budget: ')
        budget_info.grid(row=9, column=0, sticky='we')

        rating_info = Label(mainframe, text='Rating:')
        rating_info.grid(row=10, column=0, sticky='we')

        error = Label(mainframe, text='', fg='red')
        error.grid(row=3, columnspan=3, column=0, sticky='we')

    elif option == 'Games':
        text_entry = ttk.Entry(mainframe)
        text_entry.grid(row=4, column=0, columnspan=4, sticky='we')

        search_button = ttk.Button(mainframe, text='SEARCH...', command=get_pair)
        search_button.grid(row=5, column=0, sticky='we')

        add_button = ttk.Button(mainframe, text='ADD', command=add_pair)
        add_button.grid(row=5, column=1, sticky='we')

        delete_button = ttk.Button(mainframe, text='DELETE', command=delete_pair)
        delete_button.grid(row=5, column=2, sticky='we')

        update_button = ttk.Button(mainframe, text='UPDATE', command=update_pair)
        update_button.grid(row=5, column=3, sticky='we')

        publisher_info = Label(mainframe, text='Publisher: ')
        publisher_info.grid(row=6, column=0, sticky='we')

        genre1_info = Label(mainframe, text='Genre: ')
        genre1_info.grid(row=7, column=0, sticky='we')

        mode_info = Label(mainframe, text='Mode: ')
        mode_info.grid(row=8, column=0, sticky='we')

        rating1_info = Label(mainframe, text='Rating:')
        rating1_info.grid(row=9, column=0, sticky='we')

        empty = Label(mainframe, text='')
        empty.grid(row=10, column=0, sticky='we')

        error = Label(mainframe, text='', fg='red')
        error.grid(row=3, columnspan=3, column=0, sticky='we')

    elif option == 'Books':
        text_entry = ttk.Entry(mainframe)
        text_entry.grid(row=4, column=0, columnspan=4, sticky='we')

        search_button = ttk.Button(mainframe, text='SEARCH...', command=get_pair)
        search_button.grid(row=5, column=0, sticky='we')

        add_button = ttk.Button(mainframe, text='ADD', command=add_pair)
        add_button.grid(row=5, column=1, sticky='we')

        delete_button = ttk.Button(mainframe, text='DELETE', command=delete_pair)
        delete_button.grid(row=5, column=2, sticky='we')

        update_button = ttk.Button(mainframe, text='UPDATE', command=update_pair)
        update_button.grid(row=5, column=3, sticky='we')

        writer_info = Label(mainframe, text='Writer: ')
        writer_info.grid(row=6, column=0, sticky='we')

        length_info = Label(mainframe, text='Length: ')
        length_info.grid(row=7, column=0, sticky='we')

        genre_info = Label(mainframe, text='Genre: ')
        genre_info.grid(row=8, column=0, sticky='we')

        rating_info = Label(mainframe, text='Rating:')
        rating_info.grid(row=9, column=0, sticky='we')

        empty1 = Label(mainframe, text='')
        empty1.grid(row=10, column=0, sticky='we')

        error = Label(mainframe, text='', fg='red')
        error.grid(row=3, columnspan=3, column=0, sticky='we')

option_copy = ''
entry_copy = None

 # MAIN VISUAL
root = Tk()
root.title("Collection")
root.geometry('600x400')

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky='nsew')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = Label(mainframe, text='Please select what are you looking for: ')
text.grid(row=0, columnspan=3, column=0, sticky='we')

movie_option = ttk.Button(mainframe, text='MOVIES', command=lambda: select_option('Movies'))
movie_option.grid(row=2, column=0, sticky='we')

game_option = ttk.Button(mainframe, text='GAMES', command=lambda: select_option('Games'))
game_option.grid(row=2, column=1, sticky='we')

book_option = ttk.Button(mainframe, text='BOOKS', command=lambda: select_option('Books'))
book_option.grid(row=2, column=2, sticky='we')

root.mainloop()

with open('movies.txt', 'w') as movies:
    movies.write(str(Movies.movie_dict))

with open('books.txt', 'w') as books:
    books.write(str(Books.books_dict))

with open('computer_games.txt', 'w') as games:
    games.write(str(ComputerGames.games_dict))
