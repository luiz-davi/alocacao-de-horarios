from factory.grade import exec
import os
import sys

# Obter o caminho absoluto da pasta 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '.')
sys.path.append(src_path)


docentes, cadeiras = exec()

print(docentes[0].nome)
print(cadeiras[0].nome)
