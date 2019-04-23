#importowanie bibliotek i fukcji 
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout,QColorDialog,QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt

#stworzenie okna
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        #zaimplementowanie Przycisków, pól, okienek i podpisów dla współrzędnych
        self.button = QPushButton('Rysuj', self)
        self.xlabel = QLabel("XA", self)
        self.xEdit = QLineEdit()
        self.ylabel = QLabel("YA", self)
        self.yEdit = QLineEdit()
        self.xlabel1 = QLabel("XB", self)
        self.xEdit1 = QLineEdit()
        self.ylabel1 = QLabel("YB", self)
        self.yEdit1 = QLineEdit()
        self.xlabel2 = QLabel("XC", self)
        self.xEdit2 = QLineEdit()
        self.ylabel2 = QLabel("YC", self)
        self.yEdit2 = QLineEdit()
        self.xlabel3 = QLabel("XD", self)
        self.xEdit3 = QLineEdit()
        self.ylabel3 = QLabel("YD", self)
        self.yEdit3 = QLineEdit()
        
        #stworzenie przycisków do wyboru koloru oraz wczytywania danych z oddzielnego pliku
        self.clrChoose=QPushButton('Wybierz kolor wykresu', self)
        self.loadData=QPushButton('Wczytaj dane', self)
        
        #stworzenie okienek i podpisów dla współrzędnych punktu P
        self.info = QLabel ("Informacje o Punkcie P", self)
        self.xlabel4 = QLabel("XP",self)
        self.xlabel5 = QLabel()
        self.ylabel4 = QLabel("YP",self)
        self.ylabel5 = QLabel()
        self.informacja = QLabel()
        
        #stworzenie przycisku do usuwania danych 
        self.button1 = QPushButton('Usuń dane', self)
        #stworzenie przycisku do zapisywania danych do pliku
        self.button2 = QPushButton('Zapisz dane w pliku tekstowym', self)
        
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        # ladne ustawienie i wysrodkowanie
        layout =  QGridLayout(self)
        
        #umiejscowienie okienek i podpisów dla współrzędnych
        layout.addWidget(self.xlabel, 1, 1)
        layout.addWidget(self.xEdit, 1, 2)
        layout.addWidget(self.ylabel, 2, 1)
        layout.addWidget(self.yEdit, 2, 2)
        
        layout.addWidget(self.xlabel1, 3, 1)
        layout.addWidget(self.xEdit1, 3, 2)
        layout.addWidget(self.ylabel1, 4, 1)
        layout.addWidget(self.yEdit1, 4, 2)
        
        layout.addWidget(self.xlabel2, 5, 1)
        layout.addWidget(self.xEdit2, 5, 2)
        layout.addWidget(self.ylabel2, 6, 1)
        layout.addWidget(self.yEdit2, 6, 2)
        
        layout.addWidget(self.xlabel3, 7, 1)
        layout.addWidget(self.xEdit3, 7, 2)
        layout.addWidget(self.ylabel3, 8, 1)
        layout.addWidget(self.yEdit3, 8, 2)
        
        
        #umiejscowienie podpisów i przycisków dotyczących punktu P
        layout.addWidget(self.info, 1, 3)
        layout.addWidget(self.xlabel4, 2, 3)
        layout.addWidget(self.xlabel5, 3, 3)
        layout.addWidget(self.ylabel4, 2, 4)
        layout.addWidget(self.ylabel5, 3, 4)
        layout.addWidget(self.informacja, 4, 3)
        
        layout.addWidget(self.button1, 6, 3, 1, -1)
        layout.addWidget(self.button2, 5, 3, 1, -1)
        
        layout.addWidget(self.button, 10, 1, 1, -1) 
        layout.addWidget(self.canvas, 9, 1, 1, -1)
        layout.addWidget(self.clrChoose, 11, 1, 1, -1)
        layout.addWidget(self.loadData, 12, 1, 1, -1)
        
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        self.loadData.clicked.connect(self.loadDatA)
        self.button1.clicked.connect(self.usun)
        self.button2.clicked.connect(self.zapisz)
        
    def checkValues(self,lineE):
        if lineE.text().lstrip('-').replace('.','').isdigit():
            return float (lineE.text())
        
    #zdefiniowanie metody rysowania wykresu    
    def rysuj(self,clr='m'):
        x=self.checkValues(self.xEdit)
        y=self.checkValues(self.yEdit)
        
        x1 = self.checkValues(self.xEdit1)
        y1 = self.checkValues(self.yEdit1)
        
        x2 = self.checkValues(self.xEdit2)
        y2 = self.checkValues(self.yEdit2)
        
        x3 = self.checkValues(self.xEdit3)
        y3 = self.checkValues(self.yEdit3)
        
        P1, P2=[x, x1],[y, y1]
        P3, P4=[x2, x3],[y2, y3]
        
        S=[x,y,
           x1,y1,
           x2,y2,
           x3,y3]
        M=(S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4])

        if M != 0:
            t1=((S[4]-S[0])*(S[7]-S[5])-(S[5]-S[1])*(S[6]-S[4]))/((S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4]))
            t2=((S[4]-S[0])*(S[3]-S[1])-(S[5]-S[1])*(S[2]-S[0]))/((S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4]))       
            XP=S[4]+t2*(S[6]-S[4])
            YP=S[5]+t2*(S[7]-S[5])
            #sprawdzenie, w którym miejscu znajduje się punkt P
            if t1>=0 and t1<=1 and t2>=0 and t2<=1:
                self.xlabel5.setText(str('{:.3f}'.format(XP)))
                self.ylabel5.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przecięciu dwóch odcinków')
            elif 0<=t1<=1:
                self.xlabel5.setText(str('{:.3f}'.format(XP)))
                self.ylabel5.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przedłużeniu odcinka CD')
            elif 0<=t2<=1: 
                self.xlabel5.setText(str('{:.3f}'.format(XP)))
                self.ylabel5.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przedłużeniu odcinka AB')
            else:
                self.xlabel5.setText(str('{:.3f}'.format(XP)))
                self.ylabel5.setText(str('{:.3f}'.format(YP)))
                self.informacja.setText('Na przedłużeniu obu odcinków')
        
        #sprawdzneie czy nie dzielimy przez zero
        else:
            msg_err = QMessageBox()
            msg_err.setIcon(QMessageBox.Warning)
            msg_err.setWindowTitle('Błąd')
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText('Dzielenie przez zero. Nie można obliczyć współrzędnych punktu przecięcia. Wprowadź inne współrzędne.')
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
        
        if x != None and y !=None:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y, 'o',color=clr)
            ax.text(x,y,'A['+str(x)+','+str(y)+']')
            ax.plot(x1, y1, 'o', color=clr)
            ax.text(x1,y1,'B['+str(x1)+','+str(y1)+']')
            ax.plot(x2, y2, 'o', color=clr)
            ax.text(x2,y2,'C['+str(x2)+','+str(y2)+']')
            ax.plot(x3, y3, 'o', color=clr)
            ax.text(x3,y3,'D['+str(x3)+','+str(y3)+']')
            ax.plot((x,x1), (y,y1),'-',color=clr)
            ax.plot((x2,x3), (y2,y3),'-',color=clr)
            if M != 0:
                ax.plot(XP,YP,'o',color='black')
                ax.text(XP,YP,'P['+str('{:.3f}'.format(XP))+','+str('{:.3f}'.format(YP))+']')
                ax.plot((x,XP), (y,YP),'--',dashes=(1,5),color=clr)
                ax.plot((x1,XP),(y1,YP),'--',dashes=(1,5),color=clr)
                ax.plot((x2,XP),(y2,YP),'--',dashes=(1,5),color=clr)
                ax.plot((x3,XP),(y3,YP),'--',dashes=(1,5),color=clr)
                #plt.plot(P1, P2, P3, P4, marker='o', color=clr)
                #plt.plot(XP,YP,'o','k')
                #plt.plot(P1, P2, XP, YP,'--','k')
            self.canvas.draw() 
        #sprawdzenie czy dane zostały wprowadzone poprawnie    
        else:
            msg_err = QMessageBox()
            msg_err.setIcon(QMessageBox.Warning)
            msg_err.setWindowTitle('Błąd')
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText('Wprowadzono niepoprawne współrzędne')
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
            

            
    #metoda rysująca wykres    
    def handleButton(self):
        self.rysuj()
        
    #metoda która pozwala wybrać kolor wykresu    
    def clrChooseF(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.rysuj(color.name())
            
    #zdefiniowanie funkcji która wczytuje dane z oddzielmego pliku        
    def loadDatA(dane):
        plik=open(dane,'r')
        wiersze=plik.readlines()
        plik.close()
        
    # zdefiniowanie funkcji która usuwa dane z okienek i wykresu   
    def usun(self):
        self.xEdit.clear()
        self.yEdit.clear()
        self.xEdit1.clear()
        self.yEdit1.clear()
        self.xEdit2.clear()
        self.yEdit2.clear()
        self.xEdit3.clear()
        self.yEdit3.clear()
        self.xlabel5.clear()
        self.ylabel5.clear()
        self.informacja.clear()
        self.figure.clear()
    
    #zdefiniowanie funkcji która zapisuje wyniki do pliku    
    def zapisz(self):
        wyniki = open('wyniki.txt','a')
        wyniki.write(55*'*')
        wyniki.write('\n|{:^10}|{:^10}|{:^30}|\n'.format('XP', 'YP', 'Informacja o punkcie P'))
        wyniki.write(55*'*')
        wyniki.write('\n|{:^10}|{:^10}|{:^30}|\n'.format(self.xlabel5.text(),self.ylabel5.text(), self.informacja.text()))
        wyniki.write(55*'*')

if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app=QApplication.instance()
    window = Window()
    window.show()
    sys.exit(app.exec_())

        