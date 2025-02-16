import csv
import os

class DataReader:
    @staticmethod #metoda ktora jest w klasie a nie w obiekcie
    def get_csv_data(filename):
        """

        :param filename:
        :return:
        """
        # Get the absolute path of the project directory
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) # This gets the current script directory
        # Construct the path to the CSV file // gdyby powyższa zmienna była użyta w innej lokalizacji, np. w Demoblaze, można podać dodatkowe argumenty: CSV_PATH = os.path.join(PROJECT_DIR, "test_data", "valid_login_credentials.csv")
        CSV_PATH = os.path.join(PROJECT_DIR, filename)
        rows = []
        # "r" read
        with open(CSV_PATH, "r") as data_file:
            reader = csv.reader(data_file)
            #Pomiń pierwszy wiersz (nagłówki w csv)
            next(reader, None)
            for row in reader:
                rows.append(row)
        return rows


