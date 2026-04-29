import cv2


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Unable to open camera")
    else:
        try: # <--- Start monitoring for interruptions
            print("Camera started. Press 'q' in the window to stop.")
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Unable to read a frame")
                    break

                cv2.imshow('Camera Feed', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        except Exception as e:
            print(f"An error occurred: {e}")
            
        finally: # <--- THIS RUNS NO MATTER WHAT
            print("Safely releasing camera resources...")
            cap.release()
            cv2.destroyAllWindows()
            print("Camera released.")