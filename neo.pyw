import virtkeyboard, subprocess, time, threading, winsound


def openNotePad():
    pad = subprocess.call("notepad.exe")


t = threading.Thread(target = openNotePad)
t.start()

time.sleep(0.5)

virtkeyboard.output("Wake up, Neo...")
time.sleep(1)
virtkeyboard.delete(15)
virtkeyboard.output("The Matrix has you...")
time.sleep(1.5)
virtkeyboard.delete(21)
virtkeyboard.output("Follow the white rabbit.")
time.sleep(1.5)
virtkeyboard.delete(24)
virtkeyboard.output("Knock, knock, Neo.")

winsound.PlaySound('knock.wav', winsound.SND_FILENAME)

