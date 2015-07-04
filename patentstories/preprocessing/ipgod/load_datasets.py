__author__ = 'Benjamin George Roberts <benjamin.roberts@anu.edu.au>'

import csv
from sys import argv
from pathlib import Path
from ..MongoSingleton import MongoSingleton

class DataSet:
    def __init__(self, dataset_path):
        """
        Load a dataset object and take its column names
        :param dataset_path: path to dataset csv
        :type dataset_file: Path
        """
        self.dataset_name = dataset_path.name.split(".")[0]
        self.dataset_file = dataset_path.open("r", encoding='latin-1')
        self.column_names = self.dataset_file.readline().strip().split(",")

    def load_to_mongo(self):
        """
        Insert the values of the dataset object into mongodb.
        Drops existing versions of the collection if present
        :return: number of entries
        :rtype: int
        """
        db = MongoSingleton.get_db()

        # Check for existing column and drop
        if db[self.dataset_name].count() == self.__get_remaining_line_count__():
            print("collection {0} already exists in database, skipping...".format(self.dataset_name))
            return 0
        else:
            print("incomplete collection {0} exists in database, dropping...".format(self.dataset_name))
            db.drop_collection(self.dataset_name)

        collection = db[self.dataset_name]
        entry_count = 0

        # Add the objects to mongo
        value_rows = csv.reader(self.dataset_file, delimiter=",", quotechar='"')
        for value_row in value_rows:
            assert(len(value_row) is len(self.column_names))

            collection.insert(dict(zip(self.column_names, value_row)))
            entry_count += 1

            if (entry_count % 1000) is 0:
                print("added {0} entries...".format(entry_count))

        print("added {0} entries to collection {1}".format(entry_count, self.dataset_name))

        return entry_count

    def __get_remaining_line_count__(self):
        """
        Gets the number of remaining lines in the file without loosing current position
        :returns: number of remaning lines
        :rtype: int
        """
        line_count = 0
        pos = self.dataset_file.tell()
        while self.dataset_file.readline():
            line_count += 1

        self.dataset_file.seek(pos)

        return line_count


def main():
    """
    Add the dataset files found in the ARGV parameter to the configured mongodb instance
    :return: None
    """
    # Check if path passed
    if len(argv) != 2:
        print("{0} dataset_path".format(argv[0]))
        exit(1)

    # Check for valid path
    path = Path(argv[1])
    if not path.exists() and path.is_dir():
        print("invalid or missing path: {0}".format(argv[1]))
        exit(1)

    # glob search for .csv's in path and add
    file_count = 0
    entry_count = 0
    for data_set_file in path.glob("IPGOD*.csv"):
        file_count += 1
        if not data_set_file.is_file():
            continue

        try:
            print("Adding dataset \"{0}\" to mongo instance".format(data_set_file.name))
            entry_count += DataSet(data_set_file).load_to_mongo()
        except IOError as e:
            print("Failed to add dataset \"{0}\" to mongo instance".format(data_set_file.name))
            print(e)

    print("{0} datasets added ({1} entries)".format(file_count, entry_count))

if __name__ == '__main__':
    main()