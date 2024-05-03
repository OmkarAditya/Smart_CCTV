import cv2
import serial

# Open serial connection to Arduino
ser = serial.Serial('COM20', 9600)  # Change '/dev/ttyACM0' to your Arduino's port

cap = cv2.VideoCapture('in.avi')
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)
    
    # Display the resulting frame
    for (x,y,w,h) in humans:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the number of people detected
    cv2.putText(frame, 'People detected: ' + str(len(humans)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

    # Print the number of people detected in the terminal
    print('People detected: ', len(humans), flush=True)

    # Send the number of people detected to Arduino
    ser.write(str(len(humans)).encode())

    cv2.imshow('frame',frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):  # Increase the delay to 30 ms
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Close serial connection
ser.close()
