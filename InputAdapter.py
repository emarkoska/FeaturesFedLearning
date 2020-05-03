import pandas as pd
import json

class InputAdapter:
    """
    An adapter class that takes a filepath and converts
    whichever input source into a pandas dataframe.

    Example functions for json and database conversions added,
    just for illustration how this class could be further utilised.
    """
    @staticmethod
    def csv(filepath):
        return pd.read_csv(filepath)

    @staticmethod
    def json(filepath):
        """
        Untested, depends on the domain and
        knowing more about the structure of the
        incoming json files
        """
        with open(filepath) as train_file:
            dict_train = json.load(train_file)

        # converting json dataset from dictionary to dataframe
        df = pd.DataFrame.from_dict(dict_train, orient='index')
        df.reset_index(level=0, inplace=True)
        return df

    @staticmethod
    def excel(filepath):
        return pd.read_excel(filepath)

    @staticmethod
    def database(url, query):
        #run query
        #parse query result in a dataframe
        #return dataframe
        return True

