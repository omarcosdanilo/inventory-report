from inventory_report.importer.importer import Importer
from inventory_report.inventory.utils.csv_report_generator import get_csv_data


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if "csv" not in path:
            raise ValueError('Arquivo inválido')
        return get_csv_data(path)
