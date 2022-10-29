from inventory_report.inventory.utils.csv_report_generator import (
    generate_csv_report,
)
from inventory_report.inventory.utils.json_report_generator import (
    generate_json_report,
)
from inventory_report.inventory.utils.xml_report_generator import (
    generate_xml_report,
)


class Inventory:
    @staticmethod
    def import_data(path, report_type):

        if "csv" in path:
            return generate_csv_report(path, report_type)
        elif "json" in path:
            return generate_json_report(path, report_type)

        return generate_xml_report(path, report_type)
