# Extraindo e Compactando arquivos zip com Python
from zipfile import ZipFile

with ZipFile("arquivo_compactado.zip", "w") as zip:
    zip.write("arquivo1.txt")  # Escrevendo o arquivo1.txt no arquivo_compactado.zip.
    zip.write("arquivo2.txt")  # Escrevendo o arquivo2.txt no arquivo_compactado.zip.

# Extrair arquivo zip
with ZipFile("arquivo_compactado.zip", "r") as zip:
    zip.extractall("temp")  # Extrai todos os arquivos para a pasta temp.

# Extrair um arquivo zip específico
with ZipFile("arquivo_compactado.zip", "r") as zip:
    zip.extract("arquivo2.txt", "test")  # Extrai o arquivo2.txt para a pasta test.
