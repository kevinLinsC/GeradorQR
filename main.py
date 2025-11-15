import qrcode
import os
import random
from urllib.parse import urlparse


# Verifica se a URL é valida, se for retorna a URL.
def PegaURLValida():
    while True:
        # URL que será usado para fazer o qrcode.
        url = str(input("Coloque a URL: ").strip())

        try:
            resultado = urlparse(url)
            if all([resultado.scheme, resultado.netloc]):
                return url
            else:
                print("-=" * 30)
                print("URL invalida ou incompleta.")
                print("-=" * 30)
        except:
            print("URL invalida.")


def main():
    while True:
        #Limpa o terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # URL que será usado para fazer o qrcode.
        url = PegaURLValida()

        # Procura o "//" do url.
        indice_inicial = url.find("//")
        indice_final = -1

        # Se o "//" existir, acrescenta dois no indice_inicial
        # E procura "/" a apartir do indice_inicial.
        if indice_inicial != 1:
            indice_inicial = indice_inicial + 2
            indice_final = url.find("/", indice_inicial)

        # nome que será colocado no arquivo.
        nome = ""

        # Pega o nome do site para ser usado como nome do arquivo.
        if indice_inicial != -1 and indice_final != -1:
            nome = url[indice_inicial:indice_final]
        else:
            print("Digite uma URL valida.")

        # Caminho onde o qrcode será gerado.
        diretorio = "qrcodes gerados"

        # Verifica se o diretorio existe, se não existir cria o diretorio.
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print("-=" * 30)
            print(f"Diretorio {diretorio} criado com sucesso!")

        # Nome do arquivo que será gerado.
        nome_arq = nome + "_" + str(random.randint(1000, 9999)) + ".png"

        # Unindo o diretorio com o nome do arquivo.
        caminho_pasta = os.path.join(diretorio, nome_arq)

        # Objeto qrcode.
        qr = qrcode.QRCode()
        qr.add_data(url)

        img = qr.make_image() # Fazendo a imagem do qrcode.
        img.save(caminho_pasta) # Salvando o qrcode no file_path.

        print("-=" * 30)
        print("QR Code gerado com sucesso!")
        print("-=" * 30)

        # Pergunta para o usuário se ele quer continuar no programa.
        continuar = input("Deseja continuar? [S/N] ").strip().lower()[0]
        if continuar == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
            break


if __name__ == "__main__":
    main()