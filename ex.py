global installingExtension
installingExtension = False
import PyInEx.py as nowPy
import PyInEx.input as input
while True:
  if installingExtension == False:
    nowPy.defineExtension("__DEF__ [PyInEx]")
    nowPy.downloadExtension(f"$download #{nowPy.lastDefinedExtension} @as 'pie'")
    nowPy.activeExtension("pie.xts")
    installingExtension = True
