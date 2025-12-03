import csv
from abc import ABC, abstractmethod

from tabulate import tabulate


# Добавление других отчетов реализовано через принцип OCP:
# Создаются новые классы, реализующие этот интерфейс
class IReport(ABC):
    @abstractmethod
    def generate(self, files: list[str]):
        pass


class PerformanceReport(IReport):
    def generate(self, files: list[str], as_table: bool = False) -> list | str:
        positions = {}

        for file in files:
            with open(file, newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    pos = row["position"]
                    perf = float(row["performance"])

                    total, count = positions.get(pos, [0, 0])
                    positions[pos] = [total + perf, count + 1]

        # Вычисление среднего значения по позициям
        for k in positions.keys():
            positions[k] = round(positions[k][0] / positions[k][1], 2)

        rows = list(sorted(positions.items(), key=lambda x: x[1], reverse=True))

        return self._draw_table(rows) if as_table else rows

    def _draw_table(self, positions: list) -> str:
        return tabulate(
            positions,
            headers=["position", "performance"],
            showindex=range(1, len(positions) + 1),
        )


# Заглушка для другого отчета
class SkillQtyReport(IReport):
    def generate(self, files: list[str], skill_name: str):
        pass
