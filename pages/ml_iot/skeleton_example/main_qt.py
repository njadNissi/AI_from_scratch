# Add this if you want PyQtGraph instead of Matplotlib
import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets

class SkeletonViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.graphWidget = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.graphWidget)
        self.view = self.graphWidget.addPlot()
        self.view.setAspectLocked(True)
        self.view.setRange(xRange=(-300,300), yRange=(-100,600))
        
        # Add lines and scatter
        self.lines = []
        for _ in CONNECTIONS:
            line = pg.PlotDataItem(pen=pg.mkPen('r', width=3))
            self.view.addItem(line)
            self.lines.append(line)
        self.scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush('b'))
        self.view.addItem(self.scatter)
        
        # Timer for updates
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(30)  # 30ms = ~33 FPS

    def update_plot(self):
        with data_lock:
            data = joint_data.copy()
        for i, (start, end) in enumerate(CONNECTIONS):
            self.lines[i].setData(
                [data[start,0], data[end,0]],
                [data[start,1], data[end,1]]
            )
        self.scatter.setData(data[:,0], data[:,1])

# Then start the app:
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    viewer = SkeletonViewer()
    viewer.show()
    serial_thread = threading.Thread(target=read_serial, daemon=True)
    serial_thread.start()
    app.exec_()
    running = False
    serial_thread.join()