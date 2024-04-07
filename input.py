import PyInEx.ex as ex
global baseSettings
baseSettings = {
  "textTab": False,
  "wheterToRepeat": False,
  "seeLineNumber": False
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
  if settings.get("seeLineNumber") is False:
    if wheterToRepeat is False or settings.get("wheterToRepeat") is False:
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
  else:
    #######################################################
        if wheterToRepeat is False or settings.get("wheterToRepeat") is False:
          if repeatNumber == "#":
            if settings.get("textTab") is False:
              print("YOU MUST SET FUNCTION 'textTab' TO TRUE")
              pass
            else:
              linia = 0
              while True:
                linia = linia + 1
                alwaysInput.append(input(f"{linia}       "))
          else:
            if settings.get("textTab") is False:
              for i in range(repeatNumber):
                alwaysInput.append(input())
            else:
              linia = 0
              for i in range(repeatNumber):
                linia = linia + 1
                alwaysInput.append(input(f"{linia}       "))
        else:
          if not repeatNumber == "#":
            if settings.get("textTab") is False:
              print("YOU MUST SET FUNCTION 'textTab' TO TRUE")
            else:
              linia = 0
              for i in range(repeatNumber):
                linia = linia + 1
                napis = input(f"{linia}       ")
                napis = napis.replace("       ", "")
                print(f"Written '{napis}' in input {i+1}/{repeatNumber}")
          else:
            if settings.get("textTab") is False:
              print("YOU MUST SET FUNCTION 'textTab' TO TRUE")
            else:
              i = 0
              linia = 0
              while True:
                linia = linia + 1
                i = i + 1
                napis = input(f"{linia}       ")
                napis = napis.replace("       ", "")
                print(f"Written '{napis}' in input [{i}/999999]")
                if i == 999999:
                  pass

  
