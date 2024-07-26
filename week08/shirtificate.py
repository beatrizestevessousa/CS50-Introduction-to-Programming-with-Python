from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

name = input("Name: ")

pdf = PDF()
pdf.add_page(orientation="P", format="A4")
pdf.cell(0, 213, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
