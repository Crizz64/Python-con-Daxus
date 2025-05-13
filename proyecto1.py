#! pip install fpdf
#! m pip install upgrade pip

from fpdf import FPDF

name = input("Ingrese su nombre")
age = int(input('ingrese su edad'))

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
pdf.set_font_size(30)
pdf.image()

pdf.text(90, 145, name)
pdf.text(90, 160, age)

pdf.output("Presupuesto.pdf")