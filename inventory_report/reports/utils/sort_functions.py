from datetime import datetime

data = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-06",
        "data_de_validade": "2023-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
    {
        "id": "3",
        "nome_do_produto": "NITROUS OXIDE",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2020-12-22",
        "data_de_validade": "2024-11-07",
        "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
        "instrucoes_de_armazenamento": "instrucao 3",
    },
    {
        "id": "4",
        "nome_do_produto": "Norepinephrine Bitartrate",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2020-12-24",
        "data_de_validade": "2025-08-19",
        "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
        "instrucoes_de_armazenamento": "instrucao 4",
    },
    {
        "id": "5",
        "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
        "nome_da_empresa": "Moore Medical LLC",
        "data_de_fabricacao": "2021-04-14",
        "data_de_validade": "2025-01-14",
        "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
        "instrucoes_de_armazenamento": "instrucao 5",
    },
    {
        "id": "6",
        "nome_do_produto": "Silicea Belladonna",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2021-07-18",
        "data_de_validade": "2024-10-05",
        "numero_de_serie": "FR57 7414 7254 046O IHVX AV6L H71",
        "instrucoes_de_armazenamento": "instrucao 6",
    },
    {
        "id": "7",
        "nome_do_produto": "Spironolactone",
        "nome_da_empresa": "REMEDYREPACK",
        "data_de_fabricacao": "2021-07-17",
        "data_de_validade": "2023-11-18",
        "numero_de_serie": "SM28 B981 5118 903W JY0C 5KVO 3QD",
        "instrucoes_de_armazenamento": "instrucao 7",
    },
    {
        "id": "8",
        "nome_do_produto": "Aspirin",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2021-02-22",
        "data_de_validade": "2024-03-14",
        "numero_de_serie": "KZ63 800H NM4B ZOWB YYUI",
        "instrucoes_de_armazenamento": "instrucao 8",
    },
    {
        "id": "9",
        "nome_do_produto": "eucalyptus globulus",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-09-06",
        "data_de_validade": "2024-05-21",
        "numero_de_serie": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
        "instrucoes_de_armazenamento": "instrucao 9",
    },
    {
        "id": "10",
        "nome_do_produto": "Titanium Dioxide",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-08",
        "data_de_validade": "2023-12-08",
        "numero_de_serie": "FR29 5791 5333 58XR G4PR IG28 D08",
        "instrucoes_de_armazenamento": "instrucao 10",
    },
]


def sort_by_factory_date(products):
    factory_dates = [product["data_de_fabricacao"] for product in products]

    return sorted(
        factory_dates, key=lambda date: datetime.strptime(date, "%Y-%m-%d")
    )[0]


def sort_by_expiration_date(products):
    expiration_dates = [product["data_de_validade"] for product in products]

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


def get_company_product_quantity(products):
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

    formated = [
        f"- {company}: {quantity}\n"
        for company, quantity in occurrencies.items()
    ]

    return formated
