from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    products = [
        {
            "id": "1",
            "nome_do_produto": "Produto",
            "nome_da_empresa": "Empresa",
            "data_de_fabricacao": "2023-02-06",
            "data_de_validade": "2023-04-06",
            "numero_de_serie": "34",
            "instrucoes_de_armazenamento": "Instrução",
        },
        {
            "id": "2",
            "nome_do_produto": "Produto",
            "nome_da_empresa": "Empresa 2",
            "data_de_fabricacao": "2024-02-06",
            "data_de_validade": "2024-04-06",
            "numero_de_serie": "34",
            "instrucoes_de_armazenamento": "Instrução",
        },
        {
            "id": "3",
            "nome_do_produto": "Produto",
            "nome_da_empresa": "Empresa",
            "data_de_fabricacao": "2021-02-06",
            "data_de_validade": "2021-04-06",
            "numero_de_serie": "34",
            "instrucoes_de_armazenamento": "Instrução",
        },
    ]

    most_popular_company = "Empresa"
    oldest_manufacturing_date = "2021-02-06"
    earliest_expiration_date = "2023-04-06"

    simpleReport = ColoredReport(SimpleReport)

    report = simpleReport.generate(products)

    assert "\033[32mData de fabricação mais antiga:\033[0m" in report
    assert "\033[32mData de validade mais próxima:\033[0m" in report
    assert "\033[32mEmpresa com mais produtos:\033[0m" in report
    assert f"\033[36m{oldest_manufacturing_date}\033[0m\n" in report
    assert f"\033[36m{earliest_expiration_date}\033[0m\n" in report
    assert f"\033[31m{most_popular_company}\033[0m" in report
