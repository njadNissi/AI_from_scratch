import cv2
from ultralytics import YOLO

# 加载预训练的 YOLOv8 模型
model = YOLO('yoloe-11s-seg-pf.pt')

# 打开摄像头，0 表示默认摄像头
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 读取一帧视频
    success, frame = cap.read()

    if success:
        # 进行目标检测
        results = model(frame)

        # 可视化检测结果
        annotated_frame = results[0].plot()

        # 显示带有检测结果的帧
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # 按 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # 如果无法读取帧，退出循环
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
