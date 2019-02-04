"""
Using a fake robot as the receiver of messages.
"""

# DOne: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# TODO: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time

def main():
    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=10)
    frame.grid()

    # -------------------------------------------------------------------------
    # This example puts the widgets in a 3-column, 2-row grid
    # with some of the grid-places empty.  Here are the WIDGETS:
    # -------------------------------------------------------------------------

    label = ttk.Label(frame, text="movement")
    entry_box = ttk.Entry(frame)
    entry_box2 = ttk.Entry(frame)

    button1 = ttk.Button(frame, text="forward")
    button1['command'] = (lambda: send_it(entry_box,entry_box2))


    # -------------------------------------------------------------------------
    # Here is the use of GRID with rows and columns:
    # -------------------------------------------------------------------------
    label.grid(row=0, column=0)
    entry_box.grid(row=1, column=0)
    entry_box2.grid(row=1,column=1)
    button1.grid(row=0, column=1)
    root.mainloop()

def send_it(x,y):
    mqtt_client = com.MqttClient()
    mqtt_client.connect('Kirk', 'Preston')
    time.sleep(1)  # Time to allow the MQTT setup.
    mqtt_client.send_message('handle_forward',[x.get(),y.get()])
    print()

main()