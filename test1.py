import time
def processingPleaseWait(text, function):
    import tkinter, time, threading
    window = tkinter.Toplevel() # or tkinter.Tk()
    # code before computation starts
    label = tkinter.Label(window, text = text)
    label.pack()
    done = []
    def call():
        result = function()
        done.append(result)

    thread = threading.Thread(target = call)
    thread.start() # start parallel computation
    while thread.is_alive():
        # code while computing
        window.update()
        time.sleep(0.001)
    # code when computation is done
    label['text'] = str(done)

processingPleaseWait('waiting..', lambda: time.sleep(2))