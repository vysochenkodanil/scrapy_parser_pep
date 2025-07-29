from collections import defaultdict
from datetime import datetime
from pathlib import Path

from scrapy.utils.project import get_project_settings


class PepParsePipeline:
    def __init__(self):
        self.status_counts = defaultdict(int)

    def open_spider(self, spider):
        settings = get_project_settings()
        results_path = Path(settings.get("RESULTS_DIR", "results"))
        results_path.mkdir(parents=True, exist_ok=True)
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        settings = get_project_settings()
        results_path = Path(settings.get("RESULTS_DIR", "results"))
        results_path.mkdir(exist_ok=True, parents=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = results_path / f'status_summary_{timestamp}.csv'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = sum(self.status_counts.values())
            for status, count in self.status_counts.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{total}\n')
