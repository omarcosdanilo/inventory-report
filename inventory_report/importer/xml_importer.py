from inventory_report.importer.importer import Importer
from inventory_report.inventory.utils.xml_report_generator import get_xml_data


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if "xml" not in path:
            raise ValueError("Arquivo inválido")
        return get_xml_data(path)
