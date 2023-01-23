import os
from tabulate import tabulate
from docxtpl import DocxTemplate
from docx2pdf import convert
# Parametros
import tabula

# Documento de contrato o informe de comprarción (# pip install docxtpl)
current_working_directory = os.getcwd()
# print(current_working_directory) # should print the cwd

# Completamos la plantilla 
doc = DocxTemplate("words/Solicitud_Cambio_Potencia.docx")

context = {"P1": "15", "P2": "15", "P3": "17.5", "P4": "20", "P5": "20", "P6": "21.5", 
           "CUPS": "567891234ES", "NOMBRE_APELLIDO": "Alfonso Espinosa de los Monteros", 
           "NIF": "54212018Y"
           }

doc.render(context)
doc.save("word_solicitudCambioPotencia.docx")

# Paso de Word a Pdf
inputFile = "word_solicitudCambioPotencia.docx"
outputFile = "word_solicitudCambioPotencia.pdf"
file = open(outputFile, "w")
file.close()

convert(inputFile, outputFile)