import input
#activeExtension   Variable
global activatedExtension
activatedExtension = None
global extensionsList
extensionsList = []
global lastExtensionDefined
def returnAlert(alert):
  print(alert)
def activeExtension(extensionName):
  global activatedExtension
  try:
    if '.xts' in extensionName:
      extensionName = extensionName.replace(".xts", "")
      if extensionName in extensionsList:
        activatedExtension = f"Activated extension [{extensionName}]"
        returnAlert(activatedExtension)

        
  except:
    activatedExtension = "__% __% __% [.activatedError]"
    returnAlert(activatedExtension)
    
def defineExtension(code):
  global lastDefinedExtension
  global extensionsList
  if "__" in code:
    code = code.replace(' ', '')
    code = code.replace('__', '')
    code = code.replace('[', '')
    code = code.replace(']', '')
    if 'DEF' in code:
      code = code.replace('DEF', '')
      activatedExtension = f"Defined extension [{code}]"
      returnAlert(activatedExtension)
      if code not in extensionsList:
        extensionsList.append(code)
        lastDefinedExtension = code
      
      
  else:
    quit()

def downloadExtension(dKey):
  if '$download' in dKey:
    dKey = dKey.replace('$download', '')
    if '#' in dKey:
      dKey = dKey.replace('#', '')
      if ' ' in dKey:
        dKey = dKey.replace(' ', '')
        if "'" in dKey:
          dKey = dKey.replace("'", "")
          if '@as' in dKey:
            dKey = dKey.replace("@as", "_!_")
            extensionName, newExtensionName = dKey.split('_!_')
            activatedExtension = f"Downloaded extension [{extensionName} as {newExtensionName}]"
            returnAlert(activatedExtension)
            extensionsList.remove(extensionName)
            extensionsList.append(newExtensionName)
  
    
    
    
