# Espectrometro CCD
Script em python para abrir espectrometro CCD da Thorlabs e realizar a captura de dados conectados via GPIB.

## Requisitos:
Para o funcionamento do script temos os seguintes requisitos.

### Componentes
 - National instruments VISA:
       https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html#329456
 - Para o conversor NI GPIB-to-USB, você vai precisar do driver NI 488.2
       https://www.ni.com/en-us/support/downloads/drivers/download.ni-488-2.html#329025
 - Thorlabs:
       https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=3482

### Python packages
 - pyvisa:
       "pip install pyvisa"
       https://pypi.org/project/PyVISA/
 - numpy:
       "pip install numpy"
       https://pypi.org/project/numpy/
 - matplotlib:
       "pip install matplotlib"
       https://pypi.org/project/matplotlib/
 - instrumental:
       "pip install instrumental-lib"
       https://pypi.org/project/Instrumental-lib/
      

## Parametros:
Argumentos para serem passados ao script de captura de dados

 - arg[1]: 
      'identificador do instrumento OSA'
            '--adress'
            type=str 
            required=True 
 - arg[2]:
      'base name acrescido de path relativo para o arquivo de saida contendo os resultados dos dados coletados'
            '--output' 
            type=str 
            required=True
 - arg[3]:
      'Tempor antes do inicio da query'
            '--timeout' 
            type=int
            required=False