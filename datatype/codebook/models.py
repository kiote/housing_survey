import pyPdf
import re


class Codebook:

    def __init__(self):
        pdf = pyPdf.PdfFileReader(open("docs/AHS_Codebook.pdf", "rb"))

        self.variables_text = ""

        for page in pdf.pages:
            text = page.extractText()
            if "Variables Listed by Topic" in page.extractText():
                self.variables_text += text

    def get_info(self, field):
        result = re.search(field + '\s+(.*?)[A-Z\d]{2,}', self.variables_text)
        return result.group(1)
