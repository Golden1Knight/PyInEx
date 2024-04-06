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
global biggestInput
global alwaysInput
alwaysInput = []
def sI_on():
  smallInput = [input(), input(), input()]
def lI_on():
  largeInput = [input(), input(), input(), input(), input(), input(), input()]
def bI_on():
  bigInput = [input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input()]
def bII_on():
  biggestInput = [input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input(), input()]
def alwaysInputGo(repeatNumber, whether_to_display_notifications=False, settings=baseSettings):
  if whether_to_display_notifications is False:
    if settings.get("textTab") is False:
      

      for i in range(repeatNumber):
        alwaysInput.append(input())
    else:
      for i in range(repeatNumber):
        alwaysInput.append(input("       "))
  else:
    for i in range(repeatNumber):
      napis = input()
      alwaysInput.append(napis)
      print(f"Written {napis} for [{i}] times")

  
