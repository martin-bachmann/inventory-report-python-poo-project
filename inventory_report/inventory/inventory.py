import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path, type):
        with open(file_path) as file:
            data = list(csv.DictReader(file))

            if type == "completo":
                return CompleteReport.generate(data)
            elif type == "simples":
                return SimpleReport.generate(data)
