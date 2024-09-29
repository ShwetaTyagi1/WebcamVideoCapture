import cv2
import os #helps in interacting with os. functions like join, apth etc

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW) #0 for accessing primary camera ie laptop cam , 1 for accessing external camera   , second parameter is just something to resolve a warning if it pops up


#Snippet for saving the webcam video into memory
#types of format for saving vid: DIVX, XVID(best?), MJPG, X264, MWV1, MWV2
#VideoWriter function used for writing captured video to memory
#FOURCC is a 4-character code that defines how video frames are encoded and saved.
# * is an unpackig operator. it unpacks xvid into indivual srings and passes to the function. which them combines the indivual ascii value of the strings into a particular encoding sequence to save the video.
#AVI stands for Audio Video Interleave, and it is a multimedia container format. Can contain both audio video in one format

fourcc=cv2.VideoWriter_fourcc(*"XVID")

#function to have a unique file name everytime so that the videos dont keep replacing themselves. Can also use timestamp method. but her i use counter
def get_unique_filename(base_dir, base_name, extension):
    counter = 1  # Start the counter at 1
    filename = f"{base_name}_{counter}.{extension}"  # Create the first filename like 'output_1.avi'
    
    # Check if a file with the current filename exists in the specified directory
    while os.path.exists(os.path.join(base_dir, filename)): #path.join joins and makes a path on its own and adds / whereve needed
        counter += 1  # Increment the counter if the file exists
        filename = f"{base_name}_{counter}.{extension}"  # Update the filename with the new counter value
    
    # Return the full path to the unique filename
    return os.path.join(base_dir, filename)

# Define the base directory and base name for the output file
base_dir = r"C:/Users/Shweta Tyagi/Computer Vision Project outputs"
base_name = "output"
extension = "avi"

# Get a unique filename
filename = get_unique_filename(base_dir, base_name, extension)




output=cv2.VideoWriter(filename, fourcc,20.0,(550,550)) #4 parameters R to L: we can have 0 too as last parameter if incoming frames are grayscale ie we want to save gray video. else width,height  ,  frames per second, 

while cap.isOpened(): #isOpenend() returns a bool val. true means webcam is open and taking frames
    ret,frame=cap.read() 
    if ret==True: #true value in ret means frames are being read
        frame=cv2.resize(frame, (550,550))
        
        #can also flip 
        #frame = cv2.flip(frame,0)
        
        #can do gray scale also. need to make another gray variable with associated fucntion (above) and pass gray instead of frame. and also add 0  upar
        
        cv2.imshow("frame", frame)
        output.write(frame)
        k=cv2.waitKey(1) #1 means dynamic, not static image
        if k==ord('q') & 0xFF:
            break
      
#if these two statements are written with wrong indentation ie in while loop for example camera will only be open for a short while        
cap.release() #ALWAYS RELEASE VID FROM CAPTURED OBJECT 
output.release()
cv2.destroyAllWindows()
        
