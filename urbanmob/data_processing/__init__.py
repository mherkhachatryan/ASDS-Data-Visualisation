from data_processing.transformation import DataTransform
from urbanmob import data_path

data = DataTransform(data_path, nrows=100).transform_data()
