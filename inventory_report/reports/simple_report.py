from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(product_list):
        company_name_list = []
        manufacturing_date_list = []
        expiration_date_list = []
        today = datetime.now().strftime("%Y-%m-%d")

        for product in product_list:
            company_name_list.append(product["nome_da_empresa"])
            manufacturing_date_list.append(product["data_de_fabricacao"])
            if product["data_de_validade"] >= today:
                expiration_date_list.append(product["data_de_validade"])

        oldest_manufacturing_date = min(manufacturing_date_list)
        earliest_expiration_date = min(expiration_date_list)
        most_popular_company = max(
            company_name_list, key=company_name_list.count
        )

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {earliest_expiration_date}\n"
            f"Empresa com mais produtos: {most_popular_company}"
        )
