# 필요한 모듈 import
import cv2

# 얼굴이 저장된 이미지와 WebCAM 준비
template = cv2.imread('./data/image.png')
th, tw = template.shape[:2]
cv2.imshow('template', template)

webCAM = cv2.VideoCapture(0)

# 'q' 키 입력될 때까지 계속 실행
while True:

    # step1) webCAM 이미지 준비
    ret, image = webCAM.read()

    # step2) 이미지 특징 매칭
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # step3) 매칭 좌표를 이미지에 그리기
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    top_left = maxLoc
    match_val = maxVal
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
    cv2.imshow('webCAM', image)

    # 키 입력 확인
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
       
webCAM.release()
cv2.destroyAllWindows()
