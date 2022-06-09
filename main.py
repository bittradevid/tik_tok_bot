#Identifica la posicion de tu mouse  en la pantalla
print(pyautogui.position())

#Locacion del tik tok  x=720, y =531

pyautogui.moveTo(720, 531)
time.sleep(3)
pyautogui.scroll(-16)


for i in range(5):
    time.sleep(0.5)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.scroll(-16)
