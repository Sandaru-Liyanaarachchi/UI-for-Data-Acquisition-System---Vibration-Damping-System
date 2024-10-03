# UI-for-Data-Acquisition-System---Vibration-Damping-System

The data acquisition system for vibration analysis interfaces the DAQ device with a computer via a USB connection. The data received at the computer’s serial port is read by custom software developed using Python and PyQt5. This software provides a graphical user interface (GUI) to facilitate user interaction for starting, stopping, and saving the recorded vibration data.

## Detailed Explanation of UI

### 1. Initial Launch Screen
Upon launching the application, the user is greeted with the initial screen. The user must press **"Next"** to proceed.

![Initial Launch Screen](link-to-image-figure-43)

### 2. COM Port and Baud Rate Selection
In this window, the user selects the appropriate COM port and baud rate for communication. The **"Refresh"** button updates the list of available ports, and the **"Connect"** button initiates the connection.

![COM Port and Baud Rate Selection](link-to-image-figure-44)

### 3. COM Port and Baud Rate Connected
Once the correct COM port and baud rate are selected, pressing the **"Connect"** button connects the device, and the user is taken to the data collection window.

![COM Port and Baud Rate Connected](link-to-image-figure-45)

### 4. Data Collection Controls
In this window, the user can start, stop, and save the recording of acceleration data. The **"Start"** button begins data collection, the **"Stop"** button halts it, and the **"Save"** button opens a dialog to save the recorded data.

![Data Collection Controls](link-to-image-figure-46)

### 5. Start Collecting Data
When the user presses **"Start,"** the system begins collecting data, as indicated by the message **"Start collecting data..."**

![Start Collecting Data](link-to-image-figure-47)

### 6. Stop Collecting Data
Pressing **"Stop"** halts the data collection, and the message **"Stop collecting data..."** appears on the screen.

![Stop Collecting Data](link-to-image-figure-48)

### 7. Saving Data
After stopping the data collection, the user can save the data by pressing the **"Save"** button. This opens a dialog where the user can specify the file name and location.

![Saving Data](link-to-image-figure-49)

### 8. Success Message
Upon successfully saving the data, a confirmation message appears, indicating the location of the saved file.

![Success Message](link-to-image-figure-50)

### 9. Saved File Location
The saved file can be found in the specified save location.

![Saved File Location](link-to-image-figure-51)

### 10. Close the Windows
When the **"Finish"** button is clicked, all the opened windows are closed.

![Close the Windows](link-to-image-figure-52)
