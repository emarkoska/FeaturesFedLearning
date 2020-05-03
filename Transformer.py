import pandas as pd
import numpy as np

class Transformer():
    """
        A module with isolated transformations applied
        to a specific dataframe. The module is divided into transforming functions
        and pre-processing functions.

        """
    #Transforming columns
    @staticmethod
    def lookup_dictionary(dataframe, column):
        """
        Converts the column to a categorical value,
        and then replaces all categorical values with numerical ones
        """
        dataframe[column] = pd.Categorical(dataframe[column])
        series = dataframe[column].cat.codes
        print("New column created by converting categorical column %s to numerical values." % column)
        return series

    @staticmethod
    def exists(dataframe, word):
        """
        Checks whether the word value exists across all rows
        and returns a new column containing the series
        """
        series = [True if x >= 1 else False for x in np.sum(dataframe.values == word, 1)]
        print("New column created with values whether the word %s exists in the dataset per row." % str(word))
        return series

    #Preprocessing

    @staticmethod
    def pp_drop_autocorrelated(dataframe, degree_of_correlation):
        """
        Dimensionality reduction.

        Makes a matrix of correlation between columns.
        For all columns in the upper triangle, finds the one with correlation
        greater than degree_of_correlation and drops those columns.
        """
        corr_matrix = dataframe.corr().abs()
        upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

        # Find index of feature columns with correlation greater than degree_of_correlation
        to_drop = [column for column in upper_triangle.columns if
                   any(upper_triangle[column] > degree_of_correlation)]

        dataframe = dataframe.drop(dataframe[to_drop], axis=1)
        print("Dropped columns: %s" % ', '.join(map(str, to_drop)))
        return dataframe

    @staticmethod
    def pp_drop_missing_data_columns(dataframe, pr_of_missing_data):
        """
        Complete case analysis

        Drops the columns that has more than pr_of_missing_data %
        of missing data
        """
        dataframe = dataframe.loc[:, dataframe.isna().sum()/len(dataframe)*100 < pr_of_missing_data]
        print("Dropped columns with more than %s percent missing data." % str(pr_of_missing_data))
        return dataframe

    #Here we could implement more transforming or preprocessing methods, depending on what we'd need