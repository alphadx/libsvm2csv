from string import ascii_uppercase
from sys import argv
import csv

if(__name__ == "__main__"):

    if(len(argv) == 2):

        if(argv[1].split(".")[-1] == "libsvm"):

            nombreArchivo = "".join(argv[1].split(".")[:-1])

            with open("{}.libsvm".format(nombreArchivo),"r") as archivo:
                max = 0
                for i in archivo:
                    for j in i.split(" ")[1:]:
                        if(len(j) >= 3):
                            if(int(j.split(":")[0]) > max):
                                max = int(j.split(":")[0])

            features = []
            for i in range(max):
                features.append(str(i+1))
            features.append("class")

            filas = []
            with open("{}.libsvm".format(nombreArchivo),"r") as archivo:
                for i in archivo:
                    contador = 0
                    fila = []
                    buff = i.split(" ")
                    clase = int(buff[0])
                    for j in buff[1:]:
                        if(len(j) >= 3):
                            if(j.split(":")[0] == features[contador]):
                                fila.append(j.split(":")[0])
                            else:
                                while(contador < max and j.split(":")[0] != features[contador]):
                                    fila.append("0")
                                    contador += 1
                                fila.append(j.split(":")[0])
                            contador += 1
                    while(contador < max):
                        fila.append("0")
                        contador += 1
                    fila.append(ascii_uppercase[clase]) #only accept 24 classes
                    filas.append(fila)

            with open("{}.csv".format(nombreArchivo),"w") as entrada:
                salida = csv.writer(entrada)
                salida.writerow(features)
                salida.writerows(filas)

        else:
            print "File must has \"libsvm\" extention"
    else:
        print "You need a libsvm extention file as parameter"
