import pandas as pd
import json

class OutputAdapter:
    """
    An adapter class that takes a filepath and converts
    an input dataframe into the appropriate output
    """
    @staticmethod
    def csv(dataframe, filepath):
        return dataframe.to_csv(filepath)

    @staticmethod
    def json(dataframe, filepath):
        return dataframe.to_json(filepath)

    #More methods can be added
