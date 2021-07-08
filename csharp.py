import os

def lista_diretorios(diretorios):
    dires = []
    arquivos = []
    for diretorio in diretorios:
        diretorio = diretorio.split(".")
        if len(diretorio) == 1:
            dires.append(diretorio)
        else:
            arquivos.append(diretorio)
    objeto = [
        dires, arquivos
    ]
    return objeto

def apagando_exe(objeto):
    for c in objeto[1]:
        if c[1] == "exe":
            arquivo = f"{c[0]}.exe"
            os.system("del {}".format(arquivo))

def codando(objeto):
    n1 = str(input("Nome do arquivo: ")).strip() #Aqui é passado o nome do arquivo
    #n1 = "programinha" #Caso você enjoe de usar o input toda a hora, recomendo usar essa linha ao inves do input
    for c in objeto[1]:
        if c[0] == n1:
            arquivo = f"{c[0]}.cs"
            arquivo_exe = f"{c[0]}.exe"
            os.system("csc {}".format(arquivo))
            os.system(f"{arquivo_exe}")

if __name__ == "__main__":
    cwd = os.getcwd()
    diretorios = os.listdir(cwd)
    objeto = lista_diretorios(diretorios)
    apagando_exe(objeto)
    codando(objeto)
    for c in objeto[0]:
        os.chdir(str(c[0]))
        cwd = os.getcwd()
        diretorios = os.listdir(cwd)
        objeto = lista_diretorios(diretorios)
        apagando_exe(objeto)
        codando(objeto)
        os.chdir("..")
    
