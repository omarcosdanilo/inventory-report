import xmltodict
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


def get_xml_data(path):
    with open(path, mode="r") as file:
        parsed = xmltodict.parse(file.read())

    return parsed["dataset"]["record"]


def generate_xml_report(path, report_type):
    products_list = get_xml_data(path)

    if report_type == "simples":
        return SimpleReport.generate(products_list)

    return CompleteReport.generate(products_list)
