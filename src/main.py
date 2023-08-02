import os
import sys

# Obter o caminho absoluto da pasta 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '.')
sys.path.append(src_path)

from factory.grade import exec

docentes, cadeiras = exec()

print(docentes)
print(cadeiras)
