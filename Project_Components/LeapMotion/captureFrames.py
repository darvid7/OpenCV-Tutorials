
import os, sys, inspect, thread, time, cv2

# import Leap Motion files
try:
    try:
        import Leap
        from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
    except ImportError:
        sys.path.append('/Users/David/Library/Python/2.7/lib/python/site-packages/LeapMotion')
        #print(sys.path)
        import Leap
except ImportError:
    print'unable to locate path to Leap Motion SDK packages'

class MyListener():
    def on_init(self, controler):
        print 'initialized'

    def on_connect(self, controller):
        print 'Connected to d'

def main():
    listener = MyListener()
    controller = Leap.Controller()
    # receive controller events
    controller.add_listener(listener)
    print 'Press ESC to quit'
    while(1):
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            controller.remove_listener(listener)
            break
        else:
            pass

if __name__=="__main__":
    main()