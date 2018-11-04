from PyQt5 import QtCore, QtWidgets
from py import NumPlots, GE
import pyqtgraph as pq


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Variant 7 VS")
        MainWindow.resize(696, 498)

        pq.setConfigOption('background', 'w')
        pq.setConfigOption('foreground', 'k')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.err_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.err_tab.setObjectName("err_tab")
        self.mainplottab_tab = QtWidgets.QWidget()
        self.mainplottab_tab.setObjectName("mainplottab_tab")
        self.groupBox = QtWidgets.QGroupBox(self.mainplottab_tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 81, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.n_line = QtWidgets.QLineEdit(self.groupBox)
        self.n_line.setGeometry(QtCore.QRect(30, 110, 31, 20))
        self.n_line.setObjectName("n_line")
        self.n_line.setText("100")
        self.x0_line = QtWidgets.QLineEdit(self.groupBox)
        self.x0_line.setGeometry(QtCore.QRect(30, 10, 31, 20))
        self.x0_line.setObjectName("x0_line")
        self.x0_line.setText("1")
        self.xf_line = QtWidgets.QLineEdit(self.groupBox)
        self.xf_line.setGeometry(QtCore.QRect(30, 40, 31, 20))
        self.xf_line.setObjectName("xf_line")
        self.xf_line.setText("18.2")
        self.y0_line = QtWidgets.QLineEdit(self.groupBox)
        self.y0_line.setGeometry(QtCore.QRect(30, 70, 31, 20))
        self.y0_line.setObjectName("y0_line")
        self.y0_line.setText("3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 16, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 20, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 20, 21))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 90, 71, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.showNplots_button = QtWidgets.QPushButton(self.groupBox)
        self.showNplots_button.setGeometry(QtCore.QRect(14, 140, 51, 23))
        self.showNplots_button.setObjectName("showNplots_button")
        self.plots = QtWidgets.QTabWidget(self.mainplottab_tab)
        self.plots.setGeometry(QtCore.QRect(80, 0, 591, 411))
        self.plots.setObjectName("plots")
        self.solPlots_tab = QtWidgets.QWidget()
        self.solPlots_tab.setObjectName("solPlots_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.solPlots_tab)
        self.gridLayout.setObjectName("gridLayout")

        self.plot_numerical = pq.GraphicsWindow(parent=self.solPlots_tab)
        self.plot_numerical.setObjectName("plot_numerical")

        self.gridLayout.addWidget(self.plot_numerical, 0, 0, 1, 1)
        self.plots.addTab(self.solPlots_tab, "")
        self.LE_tab = QtWidgets.QWidget()
        self.LE_tab.setObjectName("LE_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.LE_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.le_win = pq.GraphicsWindow(parent=self.err_tab)
        self.gridLayout_3.addWidget(self.le_win, 0, 0, 1, 1)
        self.plots.addTab(self.LE_tab, "")
        self.err_tab.addTab(self.mainplottab_tab, "")
        self.GE_tab = QtWidgets.QWidget()
        self.GE_tab.setObjectName("GE_tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.GE_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 81, 101))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.n0_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.n0_line.setGeometry(QtCore.QRect(30, 10, 31, 20))
        self.n0_line.setObjectName("n0_line")
        self.n0_line.setText("20")
        self.N_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.N_line.setGeometry(QtCore.QRect(30, 40, 31, 20))
        self.N_line.setObjectName("N_line")
        self.N_line.setText("200")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 16, 21))
        self.label_6.setObjectName("label_6")
        self.showGE_button = QtWidgets.QPushButton(self.groupBox_2)
        self.showGE_button.setGeometry(QtCore.QRect(10, 70, 51, 23))
        self.showGE_button.setObjectName("showLE_button")

        self.ge_win = pq.GraphicsWindow(parent=self.GE_tab)

        self.ge_win.setGeometry(QtCore.QRect(90, 20, 571, 371))
        self.ge_win.setObjectName("plot_ge")
        self.err_tab.addTab(self.GE_tab, "")
        self.gridLayout_2.addWidget(self.err_tab, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.plot_numtab()
        self.plot_getab()
        self.showNplots_button.clicked.connect(self.plot_numtab)
        self.showGE_button.clicked.connect(self.plot_getab)
        self.retranslateUi(MainWindow)
        self.err_tab.setCurrentIndex(0)
        self.plots.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:10pt;\">x0</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">X</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">y0</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">N</span></p></body></html>"))
        self.showNplots_button.setText(_translate("MainWindow", "Show"))
        self.plots.setTabText(self.plots.indexOf(self.solPlots_tab), _translate("MainWindow", "Numerical Solutions"))
        self.plots.setTabText(self.plots.indexOf(self.LE_tab), _translate("MainWindow", "Local Error"))
        self.err_tab.setTabText(self.err_tab.indexOf(self.mainplottab_tab), _translate("MainWindow", "Solutions"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">n0</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">N</span></p></body></html>"))
        self.showGE_button.setText(_translate("MainWindow", "Show"))
        self.err_tab.setTabText(self.err_tab.indexOf(self.GE_tab), _translate("MainWindow", "Global Error"))

    def plot_numtab(self):
        try:
            plots = NumPlots.Plots(float(self.x0_line.text()), float(self.x0_line.text()), float(self.xf_line.text()),
                                   float(self.y0_line.text()), float(self.n_line.text()))
        except ValueError:
            plots = NumPlots.Plots(1, 1, 18.5, 3, 100)
        if hasattr(self, 'p'):
            self.le_win.removeItem(self.p)
            self.plot_numerical.removeItem(self.pn)
        self.p = self.le_win.addPlot()
        self.pn = self.plot_numerical.addPlot()
        self.p.showGrid(x=True, y=True)
        self.p.addLegend()
        self.p.plot(plots.le_eu.x, plots.le_eu.y, pen='r', name="LE for Euler")
        self.p.plot(plots.le_ie.x, plots.le_ie.y, pen='g', name="LE for IE")
        self.p.plot(plots.le_rk.x, plots.le_rk.y, pen='b', name="LE for RK")
        self.pn.showGrid(x=True, y=True)
        self.pn.addLegend()
        self.pn.plot(plots.euler.x, plots.euler.y, pen='r', name="Euler")
        self.pn.plot(plots.ie.x, plots.ie.y, pen='g', name="Improved Euler")
        self.pn.plot(plots.rk.x, plots.rk.y, pen='b', name="Runge-Kutta")
        self.pn.plot(plots.ivp.x, plots.ivp.y, pen='y', name="IVP")

    def plot_getab(self):
        try:
            plot = GE.GE(int(self.n0_line.text()), int(self.N_line.text()))
        except ValueError:
            plot = NumPlots.Plots(10, 200)
        if hasattr(self, 'ge'):
            self.ge_win.removeItem(self.ge)
        self.ge = self.ge_win.addPlot()
        self.ge.showGrid(x=True, y=True)
        self.ge.addLegend()
        self.ge.plot(plot.x, plot.ge_eu, pen='r', name="GE for Euler")
        self.ge.plot(plot.x, plot.ge_ie, pen='g', name="GE for IE")
        self.ge.plot(plot.x, plot.ge_rk, pen='b', name="GE for RK")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
