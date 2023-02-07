import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(file_path) as file:
            data = xmltodict.parse(file.read())["dataset"]["record"]
            return data
