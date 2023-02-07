import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path, type):
        with open(file_path) as file:
            if file_path.endswith(".csv"):
                data = list(csv.DictReader(file))
            elif file_path.endswith(".json"):
                data = json.load(file)
            elif file_path.endswith(".xml"):
                data = xmltodict.parse(file.read())["dataset"]["record"]

        return Inventory.generate_report(data, type)

    @staticmethod
    def generate_report(data, type):
        if type == "completo":
            return CompleteReport.generate(data)
        elif type == "simples":
            return SimpleReport.generate(data)
