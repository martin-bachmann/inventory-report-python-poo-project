from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(product_list):
        simple_response = SimpleReport.generate(product_list)

        company_name_list = [
            product["nome_da_empresa"] for product in product_list
        ]

        company_counter = Counter(company_name_list)

        company_counter_response = "Produtos estocados por empresa:\n"

        for item, count in company_counter.items():
            company_counter_response += f"- {item}: {count}\n"

        return f"{simple_response}\n" + f"{company_counter_response}"
