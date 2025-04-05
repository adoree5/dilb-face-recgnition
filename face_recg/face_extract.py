import cv2
import numpy as np

def distance(v1,v2): #计算欧式距离
    np_v1 = np.array(v1)
    np_v2 = np.array(v2)
    dist = np.linalg.norm(np_v1 - np_v2, axis=1)  #通过F范数表示距离
    return dist

def detecte(img,detector):
    # 转换为灰度图，因为Dlib的人脸检测器需要灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 使用detector进行人脸检测
    faces = detector(gray)
    return faces

def face_recg(img,face,sp,facerec,known_face_names,known_face_encodings):
    rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    shape = sp(rgb, face)
    face_descriptor = facerec.compute_face_descriptor(rgb, shape)
    # 计算 face_descriptor 与 known_face_encodings 中每个向量的距离
    face_distances = distance(known_face_encodings , face_descriptor)
    name = "Unknown"
    # 使用最近邻方法决定最佳匹配
    best_match_index = np.argmin(face_distances)
    threshod =0.4
    if face_distances[best_match_index]<threshod:
        name = known_face_names[best_match_index]
    else:
        name = "Unknown"
    return name