from inventory_report.reports.simple_report import SimpleReport
from .utils.sort_functions import (
    get_company_product_quantity,
    sort_by_factory_date,
    sort_by_expiration_date,
    get_company_with_more_products,
)


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        sorted_by_factory_date = sort_by_factory_date(products)

        sorted_by_expiration_date = sort_by_expiration_date(products)

        company_with_more_products = get_company_with_more_products(products)

        companies_with_product_quantity = ''.join(
            get_company_product_quantity(products)
        )

        return (
            f"Data de fabricação mais antiga: {sorted_by_factory_date}\n"
            f"Data de validade mais próxima: {sorted_by_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_with_product_quantity}"
        )
