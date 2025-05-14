from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# import src.people_operations as po


class PDFGenerator:
    def generate_pdf(
        self,
        nome_paciente,
        procedure_id,
        procedure_data,
        procedure_prices,
        procedure_mapping,
    ):
        """
        Gera um arquivo PDF simples com o ReportLab.
        """
        # Crie um objeto canvas
        c = canvas.Canvas(f"pdfs/{nome_paciente}-{procedure_id}.pdf", pagesize=letter)

        # Defina o título do documento
        c.setTitle(f"pdfs/{nome_paciente}-{procedure_id}.pdf")

        c.drawString(50, 750, "Nome: ")
        c.drawString(100, 750, f"{nome_paciente.upper()}")

        c.drawString(400, 750, "Médico: ")
        c.drawString(450, 750, "João Pedro Sismoto")

        c.drawString(50, 730, "Numero do procedimento: ")
        c.drawString(200, 730, f"{procedure_id.upper()}")

        c.drawString(400, 730, "Especialidade: ")
        c.drawString(490, 730, "Clinico Geral")

        c.drawString(50, 710, "Data: ")
        c.drawString(100, 710, procedure_data["date"])

        # Adicione uma imagem ao PDF
        try:
            page_width, page_height = letter
            image_width, image_height = 400, 200
            x = (page_width - image_width) / 2
            y = 510
            c.drawImage("images/all.jpeg", x, y, width=image_width, height=image_height)
        except Exception as e:
            print(f"Erro ao adicionar imagem: {e}")

        coordenadas_na_linha_cabeçalho = 500
        c.drawString(10, coordenadas_na_linha_cabeçalho, "Dente")
        c.drawString(100, coordenadas_na_linha_cabeçalho, "Regiao")
        c.drawString(200, coordenadas_na_linha_cabeçalho, "Tratamento")
        c.drawString(450, coordenadas_na_linha_cabeçalho, "Quantidade")
        c.drawString(525, coordenadas_na_linha_cabeçalho, "Valor")

        coordenadas_da_linha_info = coordenadas_na_linha_cabeçalho - 25

        c.setFont("Helvetica-Bold", 12)

        valor_total = 0

        for procedure, lista_dentes in procedure_mapping.items():
            lista_dentes_str = ", ".join(lista_dentes)
            numero_de_dentes = len(lista_dentes)
            valor = numero_de_dentes * float(procedure_prices[procedure])
            valor_total += valor

            c.drawString(10, coordenadas_da_linha_info, lista_dentes_str)
            c.drawString(100, coordenadas_da_linha_info, "Todo o dente")
            c.drawString(200, coordenadas_da_linha_info, procedure)
            c.drawString(450, coordenadas_da_linha_info, f"{numero_de_dentes}")
            c.drawString(525, coordenadas_da_linha_info, f"R${valor:.2f}")
            coordenadas_da_linha_info -= 25

        c.drawString(450, coordenadas_da_linha_info, "TOTAL:")
        c.drawString(525, coordenadas_da_linha_info, f"R${valor_total:.2f}")
        # Salve o arquivo PDF
        c.showPage()
        c.save()
        print("PDF criado com sucesso.")


if __name__ == "__main__":
    # db = po.PersonDatabase()
    # people_cpfs = db.get_all_people_names()
    pdf_gen = PDFGenerator()
    nome_paciente = "João da Silva"
    procedure_id = "123456"

    procedure_data = {
        "date": "14/05/2025",
        "procedures": {
            "18": [
                "Possui les\u00f5a de furca",
                "Tratamento endod\u00f4ntico realizado",
            ],
            "21": [
                "Possui les\u00f5a de furca",
                "Tratamento endod\u00f4ntico realizado",
            ],
            "37": ["Raiz restaurada"],
        },
        "notes": "a",
    }

    procedure_prices = {
        "Cariado (C)": 1450,
        "Possui les\u00f5a de furca": 150,
        "Tratamento endod\u00f4ntico realizado": 100,
        "Raiz restaurada": 39.99,
    }
    procedure_mapping = {
        "Possui les\u00f5a de furca": ["18", "21"],
        "Tratamento endod\u00f4ntico realizado": ["18", "21"],
        "Raiz restaurada": ["37"],
    }
    pdf_gen.generate_pdf(
        nome_paciente, procedure_id, procedure_data, procedure_prices, procedure_mapping
    )
