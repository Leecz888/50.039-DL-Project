import torch
from torch.utils.data import Dataset
import pandas as pd

class CovidCoughDataset(Dataset):
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        self.inputs = self.data["uuid"]
        self.outputs = self.data["status"]

    def __getitem__(self, index):
        x = self.inputs.iloc[index]
        y = self.outputs.iloc[index]
        return x, y
        
    def __len__(self):
        return len(self.data)
    
if __name__ == '__main__':
    print("Hello World")
         