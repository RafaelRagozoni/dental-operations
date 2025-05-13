from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# import src.people_operations as po


class PDFGenerator:
    def generate_pdf(self, nome_paciente, procedure_id, procedure_data):
        """
        Gera um arquivo PDF simples com o ReportLab.
        """
        # Crie um objeto canvas
        c = canvas.Canvas(f"{nome_paciente}-{procedure_id}.pdf", pagesize=letter)

        # Defina o título do documento
        c.setTitle(f"{nome_paciente}-{procedure_id}.pdf")

        # Adicione uma imagem ao PDF
        try:
            page_width, page_height = letter
            image_width, image_height = 400, 200
            x = (page_width - image_width) / 2
            y = 510
            c.drawImage("images/all.jpeg", x, y, width=image_width, height=image_height)
        except Exception as e:
            print(f"Erro ao adicionar imagem: {e}")

        procedure_keys = ", ".join(procedure_data["procedures"].keys())
        numero_de_dentes = len(procedure_data["procedures"].keys())
        procedure_done = procedure_data["procedures"]["21"][0]
        procedure_price = procedure_data["valor"]

        # Adicione texto ao PDF
        c.drawString(50, 750, "Nome: ")
        c.drawString(50, 730, "Numero do procedimento: ")
        c.drawString(10, 500, "Dente")
        c.drawString(110, 500, "Regiao")
        c.drawString(200, 500, "Tratamento")
        c.drawString(280, 500, "Dentista")
        c.drawString(370, 500, "Especialidade")
        c.drawString(480, 500, "Quantidade")
        c.drawString(550, 500, "Valor")
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 750, f"{nome_paciente.upper()}")
        c.drawString(200, 730, f"{procedure_id.upper()}")
        c.drawString(10, 450, procedure_keys)
        c.drawString(110, 450, "Todo o dente")
        c.drawString(200, 450, procedure_done)
        c.drawString(280, 450, "Dr. Sismoto")
        c.drawString(370, 450, "Clinico Geral")
        c.drawString(480, 450, f"{numero_de_dentes}")
        c.drawString(550, 450, f"R${procedure_price}")

        # Salve o arquivo PDF
        c.showPage()
        c.save()
        print("PDF criado com sucesso.")

    def extract_procedure_mapping(self, procedure_data):
        procedure_mapping = {}
        for tooth, procedures in procedure_data["procedures"].items():
            for procedure in procedures:
                if procedure not in procedure_mapping:
                    procedure_mapping[procedure] = []
                procedure_mapping[procedure].append(tooth)
        return procedure_mapping


if __name__ == "__main__":
    # db = po.PersonDatabase()
    # people_cpfs = db.get_all_people_names()
    pdf_gen = PDFGenerator()
    nome_paciente = "João da Silva"
    procedure_id = "123456"

    procedure_data = {
        "date": "2025-04-01T15:01:33.010493",
        "procedures": {"21": ["Cariado (C)"], "22": ["Cariado (C)"]},
        "notes": "a",
        "valor": 120,
    }

    procedure_prices = {
        "Cariado (C)": 1450,
    }

    procedure_mapping = pdf_gen.extract_procedure_mapping(procedure_data)
    print(procedure_mapping)
    pdf_gen.generate_pdf(nome_paciente, procedure_id, procedure_data)
