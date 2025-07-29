import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class PepParsePipeline:
    def open_spider(self, spider):
        self.results_dir = Path('results')
        self.results_dir.mkdir(exist_ok=True, parents=True)
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        if item.get('status'):
            self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        summary_filename = self.results_dir / f'status_summary_{timestamp}.csv'
        
        with open(summary_filename, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in sorted(self.status_counts.items()):
                writer.writerow([status, count])
            writer.writerow(['Total', sum(self.status_counts.values())])
