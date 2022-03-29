import os
import visa
import argparse
import numpy as np
import matplotlib.pyplot as plt
from instrumental import instrument, list_instruments
from instrumental.drivers.spectrometers.thorlabs_ccs import CCS

def saveOutput(fileformat, data, wls=None, filenum=None):
    with open(fileformat % filenum, 'w') as outfile:
        for wl, d in zip(wls, data):
            outfile.write('%f, %f\n' % (wl*1e9, d))

    return

def useInstrument(device, filename, num=1):
    fileformat = filename +'%04i.txt'

    out = device.take_data()

    saveOutput(fileformat, out, [0], num)

    return


def startQuery(spectrometer, filename, timeout=4000):
    startWL = float(spectrometer.query("STARTWL?"))
    stopWL = float(spectrometer.query("STOPWL?"))
    print('Amplitude da frequencia de onda: %.1f to %.1f nm' % (startWL*1e9, stopWL*1e9))
    spectrometer.timeout = timeout

    print('Capturando dados do instrumento...')
    data = spectrometer.query("TRDEF TRA, 2048; TRA?;").rstrip().split(',')
    data = np.array([float(num) for num in data])

    wls = np.linspace(startWL, stopWL, data.shape[0])

    plt.plot(wls*1e9, data)

    fileformat = filename +'%04i.txt'

    filenum = 1
    while True:
        if os.path.exists(fileformat % filenum):
            filenum += 1
        else:
            break

    print('Salvando ' + fileformat % filenum + '...')

    saveOutput(fileformat, data, wls, filenum)

    return


def main(args):
    rm = visa.ResourceManager()

    print('Dispositivos encontrados:')
    print(rm.list_resources()) 
    print('Conectando...')

    osa_address = args.adress
    output = args.output

    try:
        print('Tentando conexão com %s' % osa_address)
        osa = rm.get_instrument(osa_address)

        startQuery(osa, output)
    except:
        print('utilizando biblioteca alternativa para encontrar dispositivo')
        paramsets = list_instruments()
        print(paramsets)
        print("fornando o primeiro espectrometro")

        device = CCS()
        useInstrument(device, output)

    print('================== Finalizando! ================')




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Script para capturar dados com espectrometro CCD Thorlabs')
    parser.add_argument('--adress', type=str, required=True, help='identificador do instrumento OSA')
    parser.add_argument('--output', type=str, required=True, help='base name acrescido de path relativo para o arquivo de saida contendo os resultados dos dados coletados')
    parser.add_argument('--timeout', type=int, help='Tempor antes do inicio da query')
    args = parser.parse_args()

    main(args)