import json
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


def get_json_data(path):
    with open(path, mode="r") as file:
        data = json.load(file)

    return data


def generate_json_report(path, report_type):
    products_list = get_json_data(path)

    if report_type == "simples":
        return SimpleReport.generate(products_list)

    return CompleteReport.generate(products_list)
