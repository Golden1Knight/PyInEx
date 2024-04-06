import PyInEx as ex
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

def alwaysInputGo(repeatNumber, whether_to_display_notifications=False):
  if repeatNumber == 00:
    if whether_to_display_notifications == False:
      while True:
        alwaysInput.append(input())
    else:
      while True:
        napis = input()
        alwaysInput.append(napis)
        print(f"Written {napis} for [{i}] times")
  else:
    if whether_to_display_notifications == False:
      for i in range(repeatNumber):
        alwaysInput.append(input())
    else:
      for i in range(repeatNumber):
        napis = input()
        alwaysInput.append(napis)
        print(f"Written {napis} for [{i}] times")
