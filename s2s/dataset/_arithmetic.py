import os

from typing import Sequence
from typing import Tuple

import pandas as pd
from sklearn.metrics import accuracy_score

from s2s.dataset._base import BaseDataset
from s2s.path import DATA_PATH

class ArithmeticDataset(BaseDataset):
    def __init__(self):
        super().__init__(is_cased=False)
        df = pd.read_csv(os.path.join(DATA_PATH, 'arithmetic.csv'))
        self.src = df['src'].apply(str).apply(self.preprocess).to_list()
        self.tgt = df['tgt'].apply(str).apply(self.preprocess).to_list()

    def __len__(self) -> int:
        return len(self.tgt)

    def __getitem__(self, index: int) -> Tuple[str, str]:
        return self.src[index], self.tgt[index]

    @staticmethod
    def eval(tgt: str, pred: str) -> float:
        return float(tgt == pred)

    @staticmethod
    def batch_eval(batch_tgt: Sequence[str], batch_pred: Sequence[str]) -> float:
        return accuracy_score(batch_tgt, batch_pred)