import os
from time import sleep
from glob import glob

os.chdir(input(f"\nBaşlangıç klasörü linkini yazınız: "))
mainfile = input(f"\nAna dosyanızın ismini uzantısıyla birlikte yazınız: ")

mainfilebase = mainfile.split(".")[0]
mainfileext = mainfile.split(".")[1]

while True:
    n = len(glob(f"{mainfilebase}*.{mainfileext}"))

    fmaincontent = open(mainfile, "rb").read()
    print("Wrote from: " + mainfile)

    with open(f"{mainfilebase}-{n}.{mainfileext}", "wb") as f:
        f.write(fmaincontent)

    # os.startfile(f"{mainfilebase}-{n}.{mainfileext}")

    # Süre
    sleep(5)