
import cv2
import glob
import os


class Innerextracter():
    
    def facade(self):
        for self.imagePath in glob.glob('temp/*.png'):
            returningpath=''
            no=0
            # Get user supplied values
            #self.imagePath = 'C:\\Users\\Fayaz\\Desktop\\sss\\Faiyaz Khan Passport Photo-min.jpeg'
            self.cascPath = 'haarcascade_frontalface_default.xml'

            # Create the haar cascade
            self.faceCascade = cv2.CascadeClassifier(self.cascPath)

            # Read the image
            self.image = cv2.imread(self.imagePath)
            self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            self.faces = self.faceCascade.detectMultiScale(
                self.gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30))
            #faces variable returns such values [[35 20 58 58]]

            print ("Found {0} faces!".format(len(self.faces)))
            print('at {0}'.format(self.imagePath))
            returningpath=self.imagePath

            if len(self.faces)>0:
                print(self.faces)
                no=1
                break
            else:
                print('are yar')
                no=0
                os.remove(self.imagePath)
        if no == 1:     
            return str(returningpath)
        else:
            return ("no photo been detected")

        '''# Draw a rectangle around the faces
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow("Faces found",self. image)
            cv2.waitKey(0)'''

#Pextr().face_cascade()
