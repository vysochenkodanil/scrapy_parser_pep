from collections import defaultdict
from pathlib import Path

from scrapy.utils.project import get_project_settings


class PepParsePipeline:
    def __init__(self):
        self.status_counts = defaultdict(int)

    def open_spider(self, spider):
        settings = (
            spider.settings if hasattr(spider, "settings") else get_project_settings()
        )
        results_path = settings.get("RESULTS_DIR", "results")
        Path(results_path).mkdir(parents=True, exist_ok=True)
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item["status"]] += 1
        return item

    def close_spider(self, spider):
        settings = get_project_settings()
        results_path = settings.get("RESULTS_DIR", "results")
        total = sum(self.status_counts.values())
        with open(Path(results_path) / "status_summary.csv", "w") as f:
            f.write("Статус,Количество\n")
            for status, count in self.status_counts.items():
                f.write(f"{status},{count}\n")
            f.write(f"Total,{total}\n")
