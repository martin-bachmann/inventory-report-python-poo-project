from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "Produto"
    nome_da_empresa = "Empresa"
    data_de_fabricacao = "06/02/2023"
    data_de_validade = "06/04/2023"
    numero_de_serie = 34
    instrucoes_de_armazenamento = "Instrução"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    report = product.__repr__()

    expected = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa} com validade"
        f" até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )

    assert expected == report
