from datetime import datetime


def sort_by_factory_date(products):
    factory_dates = [product["data_de_fabricacao"] for product in products]

    return sorted(
        factory_dates, key=lambda date: datetime.strptime(date, "%Y-%m-%d")
    )[0]


def sort_by_expiration_date(products):
    expiration_dates = [
        product["data_de_validade"] for product in products
    ]

    return sorted(
        expiration_dates,
        key=lambda date: datetime.strptime(date, "%Y-%m-%d"),
    )[0]


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
