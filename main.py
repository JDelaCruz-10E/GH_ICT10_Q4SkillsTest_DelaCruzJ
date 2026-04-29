from pyscript import document, display
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

days = []
absences = []


def display(e):
    day = document.getElementById('day').value
    absence = int(document.getElementById('absence').value)

    days.append(day)
    absences.append(absence)
    
    plt.clf()
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()
    plt.show()



