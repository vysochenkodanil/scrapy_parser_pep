import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import os

from collections import defaultdict
from pathlib import Path

class PepParsePipeline:
    def open_spider(self, spider):
        Path('results').mkdir(exist_ok=True) #вот тут то и создается эта сранная директория
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.status_counts.values())
        with open('results/status_summary.csv', 'w') as f:
            f.write('Статус,Количество\n')
            for status, count in self.status_counts.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{total}\n')
