import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def get_csv_data(path):
    with open(path, mode="r") as file:
        data = csv.DictReader(file, delimiter=",", quotechar='"')

        products = list(data)

    return products


def generate_csv_report(path, report_type):
    products_list = get_csv_data(path)

    if report_type == "simples":
        return SimpleReport.generate(products_list)

    return CompleteReport.generate(products_list)
