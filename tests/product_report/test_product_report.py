from inventory_report.inventory.product import Product
from datetime import date
from pytest import fixture


product_report_mock = (
    "O produto Nicotine Polacrilex"
    f" fabricado em {date(2021, 2, 18)}"
    " por Target Corporation com validade"
    f" até {date(2023, 9, 17)}"
    " precisa ser armazenado instrucao 1."
)


@fixture
def product():
    return Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        date(2021, 2, 18),
        date(2023, 9, 17),
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )


def test_relatorio_produto(product):
    assert product_report_mock == str(product)
