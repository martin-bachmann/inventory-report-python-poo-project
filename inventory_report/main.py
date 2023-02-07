import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) != 3:
        return print("Verifique os argumentos", file=sys.stderr)

    file_type = sys.argv[1].split(".")[1]

    if file_type == "csv":
        inventory = InventoryRefactor(CsvImporter)
        report = inventory.import_data(sys.argv[1], sys.argv[2])
        print(report, end="")
    elif file_type == "json":
        inventory = InventoryRefactor(JsonImporter)
        report = inventory.import_data(sys.argv[1], sys.argv[2])
        print(report, end="")
    elif file_type == "xml":
        inventory = InventoryRefactor(XmlImporter)
        report = inventory.import_data(sys.argv[1], sys.argv[2])
        print(report, end="")
