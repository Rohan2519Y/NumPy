import cv2
import numpy as np

cap = cv2.VideoCapture(0)
F = []
while True:
    frame = cap.read()
    cv2.imshow("Camera", frame)
    F.append(frame)
    if cv2.waitKey(1) == 27:  # ESC
        break
np.save("F:/NumPy/frame.npy", F)

cap.release()
cv2.destroyAllWindows()

F = np.array(np.load('F:/NumPy/frame.npy'))

print(F.shape)
print(F.ndim)