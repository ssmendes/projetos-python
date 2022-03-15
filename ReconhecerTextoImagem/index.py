import cv2
import pytesseract

# ler a imagem
imagem = cv2.imread("desafio.png")

caminho = r"C:\Program Files\Tesseract-OCR"

# extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)
print(texto)