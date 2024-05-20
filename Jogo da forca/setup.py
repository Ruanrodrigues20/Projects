import sys
from cx_Freeze import setup, Executable

# Arquivos a serem incluídos
files = ["palavra.py"]

# Defina o executável
executables = [
    Executable("jogo.py", base=None)
]

# Opções de configuração
options = {
    "build_exe": {
        "include_files": files
    }
}

# Crie o executável
setup(
    name="forca",
    version="1.1",
    description="Meu programa",
    options=options,
    executables=executables
)
