import cv2
import ascii_main
from PIL import Image
import numpy as np
import os
import glob
from moviepy.editor import *
import shutil

def frame_preprocessing(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    return frame


def to_video_conversion(fps,dims,f_name):
    img_array = []
    print('Conversion')
    total_files=len(os.listdir(os.getcwd()+'\\Temp'))
    for i in range(0,total_files):
        img = cv2.imread(os.getcwd()+'\\Temp\\output_'+str(i)+'.jpg')
        img_array.append(img)

    out = cv2.VideoWriter('Results\\'+str(f_name),cv2.VideoWriter_fourcc(*'MP4V'), fps, dims)
    
    for i in range(len(img_array)):
        out.write(img_array[i])

    
    for file in os.listdir(os.getcwd()+'\\Temp'):
        os.remove(os.getcwd()+'\\Temp\\'+file)
    os.rmdir('Temp')
    
    


def interface_main(path,choice):
    try: 
        os.mkdir('Results')
    except:
        pass
    f_name=path.split('/')[-1]
    if choice==2:
        #Conversion to mp3 initially
        video = VideoFileClip(os.path.join(path))
        video.audio.write_audiofile(os.path.join(path.replace('.mp4','.mp3')))
        try: 
            shutil.move(path.replace('mp4','mp3'), os.getcwd()+'\\Results')
        except:
            pass
        
        
        ####################################################

        cap=cv2.VideoCapture(path)
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))+1
        fps = cap.get(cv2.CAP_PROP_FPS)
        dims=(2048,1080)

        count=0
        
        try: 
            os.mkdir('Temp')
        except:
            pass
        
        while True: 
            ret,frame=cap.read()
            if ret: 
                frame=frame_preprocessing(frame)
                frame=ascii_main.asciify_function(frame,choice,f_name)
                frame=frame.resize(dims)
                frame.save('Temp/output_'+str(count)+'.jpg')
                count+=1
                print('Extracting Frame: '+str(count)+' Total Frames: '+str(int(total)))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        
        to_video_conversion(fps,dims,f_name)

    else:
        frame=cv2.imread(path)
        frame=frame_preprocessing(frame)
        ascii_main.asciify_function(frame,choice,f_name)

    print('Completed Successfully !!')

