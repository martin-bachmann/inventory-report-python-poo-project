from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer_strategy):
        self.importer = importer_strategy
        self.data = []

    def import_data(self, file_path, type):
        data = self.importer.import_data(file_path)

        self.data += data

        if type == "completo":
            return CompleteReport.generate(self.data)
        elif type == "simples":
            return SimpleReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
