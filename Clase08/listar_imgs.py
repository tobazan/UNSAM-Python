import os
import sys

def ls(dire):
    try:
        os.chdir(dire)
        print(os.listdir(os.getcwd()))
    except:
        print('El directorio especificado no se encuentra')

if __name__ == '__main__':
    dire = sys.argv[1]
    ls(dire)

# TEST
# cli % python listar_imgs.py "../Data/ordenar/imgs"