pip install python-barcode

# import EAN13 
from barcode import EAN13

#import ImageWriter para gerar imagem
from barcode.writer import ImageWriter

number = '5901234123457'
my_code = EAN13(number, writer=ImageWriter())
my_code.save("codigo_de_barras")