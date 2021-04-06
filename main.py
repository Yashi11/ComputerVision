import cv2
g_slider_position = 0
g_slider_position = int(g_slider_position)
g_capture = None
def onTrackbarSlide(pos):
    g_capture.set(cv2.CAP_PROP_FRAME_COUNT,g_slider_position)
    pos = cv2.getTrackbarPos("Position:","Cat")
    print(pos)


ll = "Resources\cat1.mp4"
g_capture = cv2.VideoCapture(ll)
cv2.namedWindow("Cat",cv2.WINDOW_AUTOSIZE)
frames = int(g_capture.get(cv2.CAP_PROP_FRAME_COUNT))
cv2.createTrackbar("Speed:", "Cat",1, 4, onTrackbarSlide)
cv2.createTrackbar("Play:", "Cat",0, 1, onTrackbarSlide)
while(True):
    success, frame = g_capture.read()
    g_slider_position += 1
    cv2.createTrackbar("Position:", "Cat", g_slider_position, frames, onTrackbarSlide)
    cv2.imshow("frame", frame)
    s = cv2.getTrackbarPos("Speed:", "Cat")
    p = cv2.getTrackbarPos("Play:","Cat")
    if(p == 0):
        cv2.waitKey(0)
    elif cv2.waitKey(40 * s) & 0xFF == ord('e'):
        break
g_capture.release()
cv2.destroyAllWindows()


