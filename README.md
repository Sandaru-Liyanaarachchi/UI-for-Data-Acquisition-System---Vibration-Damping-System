# UI-for-Data-Acquisition-System---Vibration-Damping-System

The data acquisition system for vibration analysis interfaces the DAQ device with a computer via a USB connection. The data received at the computer’s serial port is read by custom software developed using Python and PyQt5. This software provides a graphical user interface (GUI) to facilitate user interaction for starting, stopping, and saving the recorded vibration data.

## Detailed Explanation of UI

### 1. Initial Launch Screen
Upon launching the application, the user is greeted with the initial screen. The user must press **"Next"** to proceed.

![1 Start](https://github.com/user-attachments/assets/56738538-2d12-4c03-b1d4-fcaa87ce0fd5)

### 2. COM Port and Baud Rate Selection
In this window, the user selects the appropriate COM port and baud rate for communication. The **"Refresh"** button updates the list of available ports, and the **"Connect"** button initiates the connection.

![2 Com_Manager](https://github.com/user-attachments/assets/6814959b-60c2-4b80-9460-26f4dc564268)

### 3. COM Port and Baud Rate Connected
Once the correct COM port and baud rate are selected, pressing the **"Connect"** button connects the device, and the user is taken to the data collection window.

![3 Select_Comp_port](https://github.com/user-attachments/assets/9f81a296-ddf0-4df2-bbf6-f4c87f11903c)

### 4. Data Collection Controls
In this window, the user can start, stop, and save the recording of acceleration data. The **"Start"** button begins data collection, the **"Stop"** button halts it, and the **"Save"** button opens a dialog to save the recorded data.

![79](https://github.com/user-attachments/assets/57e0dbd3-b4af-4a97-a1d7-7eb985ae877e)

### 5. Start Collecting Data
When the user presses **"Start,"** the system begins collecting data, as indicated by the message **"Start collecting data..."**

![4 Start_Data Collection](https://github.com/user-attachments/assets/aa56e7ee-0536-4f22-89ff-2a6d66633969)

### 6. Stop Collecting Data
Pressing **"Stop"** halts the data collection, and the message **"Stop collecting data..."** appears on the screen.

![5 Stop_Data_Colloection](https://github.com/user-attachments/assets/90ac387b-d7f0-4223-bf82-0707bc354962)

### 7. Saving Data
After stopping the data collection, the user can save the data by pressing the **"Save"** button. This opens a dialog where the user can specify the file name and location.

![6 Save_Data](https://github.com/user-attachments/assets/bff94f9f-9746-4602-84ec-a6cc8266fde7)

### 8. Success Message
Upon successfully saving the data, a confirmation message appears, indicating the location of the saved file.

![7 Save_CSV_File](https://github.com/user-attachments/assets/4cc83790-aab4-4806-a852-b1a959c100d5)

### 9. Saved File Location
The saved file can be found in the specified save location.

![8 Confiramation](https://github.com/user-attachments/assets/8e1e65a1-b22d-47cd-b0dc-75f77b2f4d31)

### 10. Close the Windows
When the **"Finish"** button is clicked, all the opened windows are closed.

![9 Finish](https://github.com/user-attachments/assets/1c9ef627-a377-4de3-b34a-8fca204eb3b4)
