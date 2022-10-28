from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products: list):
        sorted_by_factory_date = SimpleReport.sort_by_factory_date(products)

        sorted_by_expiration_date = SimpleReport.sort_by_expiration_date(
            products
        )

        company_with_more_products = (
            SimpleReport.get_company_with_more_products(products)
        )

        return (
            f"Data de fabricação mais antiga: {sorted_by_factory_date}\n"
            f"Data de validade mais próxima: {sorted_by_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )

    @staticmethod
    def sort_by_factory_date(products):
        factory_dates = [product["data_de_fabricacao"] for product in products]

        return sorted(
            factory_dates, key=lambda date: datetime.strptime(date, "%Y-%m-%d")
        )[0]

    @staticmethod
    def sort_by_expiration_date(products):
        expiration_dates = [
            product["data_de_validade"] for product in products
        ]

        return sorted(
            expiration_dates,
            key=lambda date: datetime.strptime(date, "%Y-%m-%d"),
        )[0]

    @staticmethod
    def get_company_with_more_products(products):
        companies = [
            product["nome_da_empresa"]
            for product in products
            if product["nome_da_empresa"] is not None
        ]
        occurrencies = {}

        for company in companies:
            if company in occurrencies:
                occurrencies[company] += 1
            else:
                occurrencies[company] = 1

        return max(occurrencies, key=occurrencies.get)
