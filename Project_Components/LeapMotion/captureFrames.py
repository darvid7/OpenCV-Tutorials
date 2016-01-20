
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

class MyListener(Leap.Listener):
    frameCount = 0

    def on_init(self, controler):
        print 'initialized'
        print self.frameCount

    def on_connect(self, controller):
        print 'Connected to Leap Motion device'

    def on_frame(self, controler):
        frame = controler.frame()
        img_list = frame.images
        left_img = img_list[0]
        right_img = img_list[1]
        print 'Frame set ' + str(self.frameCount) + 'captured'
        self.frameCount += 1
        cv2.imwrite('testL.png',left_img)
        cv2.imwrite('testR.png', right_img)



def main():
    mylistener = MyListener()
    controller = Leap.Controller()
    # receive controller events
    controller.add_listener(mylistener)

    controller.set_policy(Leap.Controller.POLICY_IMAGES)
    print 'Press ENTER to quit'


    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(mylistener)
if __name__=="__main__":
    main()