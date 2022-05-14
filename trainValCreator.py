import glob 
import argparse
import os
import random
def shuffleAndWriteVal(path, totVal):
    count = 0
    with open('train.txt','r') as source:
        data = [ (random.random(), line) for line in source ]
        random.shuffle(data)

    with open('train.txt','w') as t, open("val.txt",'w') as v:
        for _, line in data:
            if count == totVal:
                v.write(line)
            else:    
                t.write(line)
                count += 1
        
		

parser = argparse.ArgumentParser(description="Automatically train.txt and val.txt builder. Train images may be in different paths. Folder names must be images and labels")
parser.add_argument('--image_folder', type=str, nargs='+' ,required = True , help='image folder full path')
parser.add_argument('--validation_rate', type=int, required = False,default = 10, help='validation rate')

args = parser.parse_args()

image_folder_path = args.image_folder
output_path = args.output
valid_rate = args.validation_rate
totalImages = 0

with open("train.txt", 'w') as fl:
    for path in image_folder_path:	            
        for (root,dirs,files) in os.walk(path, topdown= True):
            if root.split("/")[-1] == "images":
                for f in files:
                    
                    fl.write(os.path.join(root, f))
                    fl.write('\n')
                    totalImages += 1
                    
shuffleAndWriteVal("train.txt", totalImages - int(totalImages/ valid_rate))
           
