import pandas as pd

class PlanMaster:
    def __init__(self, file_path:str):
        self.df: pd.DataFrame = pd.read_csv(file_path)