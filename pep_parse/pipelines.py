import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from scrapy.utils.project import get_project_settings


class PepParsePipeline:
    def __init__(self):
        self.status_counts = defaultdict(int)

    def open_spider(self, spider):
        settings = get_project_settings()
        results_path = settings.get("RESULTS_DIR", "results")
        Path(results_path).mkdir(parents=True, exist_ok=True)
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    # def close_spider(self, spider):
    #     settings = get_project_settings()
    #     results_path = settings.get("RESULTS_DIR", "results")
    #     total = sum(self.status_counts.values())
    #     output_path = Path(results_path) / 'status_summary.csv'

    #     with open(output_path, 'w', encoding='utf-8') as f:
    #         f.write('Статус,Количество\n')
    #         for status, count in self.status_counts.items():
    #             f.write(f'{status},{count}\n')
    #         f.write(f'Total,{total}\n')
    def close_spider(self, spider):
        # Создаем директорию results, если ее нет
        os.makedirs('results', exist_ok=True)

        # Генерируем имя файла с временной меткой
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'results/status_summary_{timestamp}.csv'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = 0
            for status, count in self.status_count.items():
                f.write(f'{status},{count}\n')
                total += count
            f.write(f'Total,{total}\n')
