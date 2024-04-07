import PyInEx.ex as ex
global baseSettings
baseSettings = {
  "textTab": False,
  "lineNumber": [0,1,2,3,4,5,6,7,8,9],
  "transparency": [0,0.5,1],
  "transparencyPercent": ["0%","50%","100%"],
  "actuallyTransparency": 1
}
global smallInput
global largeInput
global bigInput
global alwaysInput
alwaysInput = []
def sI_on():
  smallInput = [input(), input(), input()]
def lI_on():
  largeInput = [input(), input(), input(), input(), input(), input(), input()]
def bI_on():
  bigInput = [input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input()]

def alwaysInputGo(repeatNumber, wheterToRepeat=False, settings=baseSettings):
  if wheterToRepeat is False:
    if repeatNumber == "#":
      if settings.get("textTab") is False:
        while True:
          alwaysInput.append(input())
      else:
        while True:
          alwaysInput.append(input("       "))
    else:
      if settings.get("textTab") is False:
        for i in range(repeatNumber):
          alwaysInput.append(input())
      else:
        for i in range(repeatNumber):
          alwaysInput.append(input("       "))
  else:
    if not repeatNumber == "#":
      if settings.get("textTab") is False:
        for i in range(repeatNumber):
          napis = input()
          print(f"Written '{napis}' in input [{i+1}/{repeatNumber}]")
      else:
        for i in range(repeatNumber):
          napis = input("       ")
          napis = napis.replace("       ", "")
          print(f"Written '{napis}' in input {i+1}/{repeatNumber}")
    else:
      if settings.get("textTab") is False:
        i = 0
        while True:
          i = i + 1
          napis = input()
          print(f"Written '{napis}' in input [{i}/999999]")
          if i == 999999:
            pass
      else:
        i = 0
        while True:
          i = i + 1
          napis = input("       ")
          napis = napis.replace("       ", "")
          print(f"Written '{napis}' in input [{i}/999999]")
          if i == 999999:
            pass
        

  
