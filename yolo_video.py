

# from dbconnection import *

from new_project import predictcnn
# USAGE
# python yolo_video.py --input videos/airport.mp4 --output output/airport_output.avi --yolo yolo-coco

import uuid
import argparse

import time
import cv2
import os
loopstatus="f"
loopcount=0
def valssss(path):
# while True:
	loopstatus="f"
	loopcount=0
	out="No Violence"

	# qry="SELECT * FROM `videos` WHERE `video_id` NOT IN(SELECT `video id` FROM `process`)"
	# res=selectall(qry)
	lisclass=["Abuse","Arrest","Arson","Assault","Burglary","Explosion","Fighting","NormalVideos","RoadAccidents","Robbery","Shooting","Shoplifting","Stealing","Vandalism"]
	# for i in res:
	# print(i)
	# print(r"C:\Users\ASUS\Downloads\Violenece\c1\src\static\file/"+i[2])
	# vs = cv2.VideoCapture(0)
	vs = cv2.VideoCapture(path)
	writer = None
	(W, H) = (None, None)
	# try to determine the total number of frames in the video file

	counti=0
	while True:
		if loopstatus=="f":
			loopstatus=="n"
			counti=counti+1
			print("cccii",counti)
			# read the next frame from the file

			(grabbed, frame) = vs.read()

			print("==> ",counti)
			# if the frame was not grabbed, then we have reached the end
			# of the stream
			if not grabbed:
				break
			cv2.imwrite("static\\file\\sample.jpg",frame)


			ress=predictcnn("static\\file\\sample.jpg")
			print("bbb",lisclass[ress[0]])

			if lisclass[ress[0]]=="Arson" or lisclass[ress[0]]=="Fighting" or lisclass[ress[0]]=="Shooting":
				out="Violence"
				break

			
				# qry="INSERT INTO `notification` VALUES(NULL,CURDATE(),%s,%s)"
				# val=(i[1],lisclass[ress[0]])
				# result_id=iud(qry,val)
				# cv2.imwrite(r"C:\Users\ASUS\Downloads\Violenece\c1\src\static\result/"+str(uuid.uuid4())+".jpg", frame)
		else:
			print("lcccc:",loopcount)
			loopcount=loopcount+1
			if loopcount==50:
				loopcount=0
				loopstatus="f"
		cv2.imshow('frame', frame)	
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
    # After the loop release the cap object
	vs.release()
	# Destroy all the windows
	cv2.destroyAllWindows()
	return out

# outs=valssss("static/file/Rocky_takes_revenge_on_Adheera____K.G.F._2_Fight_since___Rocky_vs_Adheera.mp4")
# print("hhh",outs)
	# time.sleep(10)

# C:\Users\ASUS\Downloads\yolo_video.py