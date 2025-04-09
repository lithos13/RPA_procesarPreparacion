import Activities.fileActivities as fileAct
from decouple import config

def closeApp():
    print("Closing applications...")
    fileAct.cleanPath(config('PATH_TEMP') + "Listadepedidos__ES.xlsx")
#