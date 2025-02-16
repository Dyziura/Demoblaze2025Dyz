import csv

class DataReader:
    @staticmethod #metoda ktora jest w klasie a nie w obiekcie
    def get_csv_data(filename):
        """

        :param filename:
        :return:
        """
        rows = []
        # "r" read
        with open(filename, "r") as data_file:
            reader = csv.reader(data_file)
            #Pomiń pierwszy wiersz (nagłówki w csv)
            next(reader, None)
            for row in reader:
                rows.append(row)
        return rows


