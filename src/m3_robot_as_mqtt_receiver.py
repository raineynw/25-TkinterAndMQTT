"""
Using a Brickman (robot) as the receiver of messages.
"""

# Same as m2_fake_robot_as_mqtt_sender,
# but have the robot really do the action.
# Implement just FORWARD at speeds X and Y is enough.

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
