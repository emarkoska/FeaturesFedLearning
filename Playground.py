import Transformer
import pandas as pd
import numpy as np

###############################################################
#   A playground module just for testing and experimentation. #
#   Nothing interesting here. :)                              #
###############################################################

df = pd.read_csv('Data/cars.csv')
print(df.head())

corr_matrix = df.corr().abs()
upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

# Find index of feature columns with correlation greater than degree_of_correlation
to_drop = [column for column in upper_triangle.columns if
           any(upper_triangle[column] > 0.5)]

df.drop(df[to_drop], axis=1)
print("Dropped columns: %s" % ', '.join(map(str, to_drop)))
