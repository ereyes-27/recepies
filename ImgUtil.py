import cv2
class ExtractImg:
    """
    a partir del video, extrae el frame 50 y retorna el nombre
    de la imagen
    """
    def extraerImgFromMp4(self, videoName):
        print("ImgUtil:: videoName" + videoName)

        imgName = videoName.replace('mp4', 'jpg')
        imgName = imgName.replace('videos/', '')
        folder = "static/img/"
        folder = folder + imgName

        # taking time in seconds
        time_stamp = 20

        # converting to miliseconds
        time = time_stamp * 1000

        # providing path of the video
        video_capture = cv2.VideoCapture(videoName)

        # capturing the frame in provided time.
        video_capture.set(cv2.CAP_PROP_POS_MSEC, time)
        success, image = video_capture.read()
        if success:
            # save frame as JPEG file
            #folder nombre del archivo, image es el frame
            cv2.imwrite(folder, image)
        return folder

#img = ExtractImg()
#img.guardaVideo("videos/R3plYwOGYMs.mp4")