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
        data_file = open(filename, "r")
        reader = csv.reader(data_file)
        #Pomiń pierwszy wiersz (nagłówki w csv)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows


