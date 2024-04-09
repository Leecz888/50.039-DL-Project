import json
import torch
from torch.utils.data import Dataset, DataLoader, random_split
import pandas as pd

class CovidCoughDataset(Dataset):
    def __init__(self, filename):
        self.data = pd.read_excel(filename)
        self.inputs = self.data["Filename"]
        self.outputs = self.data["Status"]

    def __getitem__(self, index):
        x = self.inputs.iloc[index]
        y = self.outputs.iloc[index]
        return x, y
        
    def __len__(self):
        return len(self.data)
    
if __name__ == '__main__':
    
    with open("./model.conf", mode="r") as conf:
        config = json.loads(conf.read())
    
    batch_size = config["batch_size"]
    
    dataset = CovidCoughDataset('./Data/Dataset.xlsx')
    train_dataset, valid_dataset, test_dataset = random_split(dataset, [0.8, 0.1, 0.1])
    train_dataloader = DataLoader(train_dataset, batch_size = batch_size, shuffle=True)
    valid_dataloader = DataLoader(valid_dataset, batch_size = batch_size, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size = batch_size, shuffle=True)
    
    
    