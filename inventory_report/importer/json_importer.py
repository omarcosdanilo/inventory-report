from inventory_report.importer.importer import Importer
from inventory_report.inventory.utils.json_report_generator import (
    get_json_data,
)


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if "json" not in path:
            raise ValueError("Arquivo inválido")
        return get_json_data(path)
