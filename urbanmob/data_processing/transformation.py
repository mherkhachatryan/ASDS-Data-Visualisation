import pandas as pd

from urbanmob import data_path


class DataTransform:
    """
    Examples:
        >>> transform = DataTransform(data_path, nrows=100)
        >>> data = transform()
        >>> data.iloc[0, 0]
        '2016-03-14 17:24:55'
    """

    def __init__(self, path: str, **kwargs):
        self.path = path
        self.data = self._read_data(**kwargs)

    def __call__(self):
        return self.transform_data()

    def transform_data(self) -> pd.DataFrame:
        self.data = self.data[self.data.passenger_count > 0]
        self.data = self.__drop_cols(self.data)
        return self.data

    @staticmethod
    def __drop_cols(data):
        for col in data.columns:
            if "Unnamed" in col:
                data.drop(col, axis=1, inplace=True)
            if "id" in col:
                data.drop(col, axis=1, inplace=True)
        return data

    def _read_data(self, **kwargs) -> pd.DataFrame:
        data = pd.read_csv(self.path, **kwargs)
        return data
