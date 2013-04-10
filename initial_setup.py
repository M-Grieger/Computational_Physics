#!/usr/bin/python
""" Programm zur Initialisierung von IPython und Matplotlib.

    Das Farbschema bei IPython kann ausgewaehlt werden und das
    Backend fuer Matplotlib wird auf GtkAgg gesetzt.
"""
import os

import IPython

# Pfade
ipyrc_dir = os.path.expanduser("~/.ipython")
#ipyrc_system = "/var/lib/python-support/python2.6/IPython/UserConfig/"
ipyrc_system = os.path.join(IPython.__path__[0], "UserConfig")
ipyrc_src = ipyrc_dir + "/ipythonrc"
mplrc_dir = os.path.expanduser("~/.matplotlib")
mplrc_src = mplrc_dir + "/matplotlibrc"

# Konfigurationsverzeichnis anlegen
if (not os.path.exists(ipyrc_dir)) or (not os.path.exists(ipyrc_src)):
    os.mkdir(ipyrc_dir)
    os.system("cp %s/* %s" % (ipyrc_system, ipyrc_dir))

print "Hat das Terminal (d)unklen oder (h)ellen Hintergrund?"
str = raw_input('Waehlen Sie "h" oder "d" und druecken Sie <ENTER>: ')
if str.upper() == "H":
    # Setze die Farben in ipython auf LightBG
    ipyrc = open(ipyrc_src, "r").read()
    ipyrc = ipyrc.replace("\ncolors Linux", "\n#colors Linux")
    ipyrc = ipyrc.replace("\n#colors LightBG", "\ncolors LightBG")
    open(ipyrc_src, "w").write(ipyrc)
else:
    # Setze die Farben in ipython auf Linux
    ipyrc = open(ipyrc_src, "r").read()
    ipyrc = ipyrc.replace("\n#colors Linux", "\ncolors Linux")
    ipyrc = ipyrc.replace("\ncolors LightBG", "\n#colors LightBG")
    open(ipyrc_src, "w").write(ipyrc)

# Konfigurationsverzeichnis anlegen
if not os.path.exists(mplrc_dir):
    os.mkdir(mplrc_dir)

# Wenn matplotlibrc noch nicht vorhanden ist, wird backend gesetzt
if os.path.exists(mplrc_src):
    print "matplotlibrc bereits vorhanden"
    print "Bitte Backend-Eintrag anpassen, oder hinzufuegen"
    print "   backend:GtkAgg "
else:
    open(mplrc_src, "w").write("backend:GtkAgg")
