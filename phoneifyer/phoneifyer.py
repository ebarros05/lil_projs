import os
from moviepy.editor import VideoFileClip
from moviepy.video.fx.crop import crop

dir_path = os.path.dirname(os.path.realpath(__file__))
inputpath = dir_path+'/input'

for f in os.listdir(inputpath):
    filename = dir_path+'/output/croppedfile_'
    vname = os.fsdecode(f)
    print(f"converting: {vname}")
    if vname.endswith('.mp4'):
        vclip = VideoFileClip(inputpath+'/'+vname)      
        w, h = vclip.size
        new_w = h * 9/16
        x1, x2 = (w - new_w)//2, (w+new_w)//2
        y1, y2 = 0, h
        cropped = crop(vclip, x1=x1, y1=y1, x2=x2, y2=y2) #x_center=w/2, y_center=h/2, width=1080, height=1920
        #cropped = cropped.resize(width=1080, height=1920)
        width, height = cropped.size
        print(width)
        print(height)
        filename = filename+vname.rstrip('.mp4')+'.mp4'
        print(filename)
        cropped.write_videofile(filename, codec='libx264')
    print("done")