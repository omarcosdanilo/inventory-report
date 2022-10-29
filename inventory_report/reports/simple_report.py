from .utils.sort_functions import (
    get_company_with_more_products,
    sort_by_expiration_date,
    sort_by_factory_date,
)


class SimpleReport:
    @staticmethod
    def generate(products: list):
        sorted_by_factory_date = sort_by_factory_date(products)

        sorted_by_expiration_date = sort_by_expiration_date(products)

        company_with_more_products = get_company_with_more_products(products)

        return (
            f"Data de fabricação mais antiga: {sorted_by_factory_date}\n"
            f"Data de validade mais próxima: {sorted_by_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
