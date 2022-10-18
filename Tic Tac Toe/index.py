
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QButtonGroup,QMessageBox


class CheckWin():
    def __init__(self, n) -> None:
        self.n = n;

    def check_diagonal_line_1(this, chooseList):
        number_of_check_diagonal = 2 * (this.n - 5) + 1;
        start_positions = {}
        tmp = tmp2 = 1
        tmp3 = this.n # store number position
        start_positions[1] = this.n;
        
        for i in range(this.n-5):
            tmp += 1
            tmp2 += this.n
            tmp3 -= 1
            start_positions[tmp] = tmp3
            start_positions[tmp2] = tmp3
        
        result = [];
        for position in start_positions:
            currentPosition = position
            line_len = start_positions[position]
            tmpArr = []
            for i in range(line_len):
                tmpArr.append(currentPosition);     
                currentPosition += (this.n + 1);
            result.append(tmpArr)
        
        num = 0;
        for sub in result:
            num = 0
            for p in sub:
                if num == 5: return True
                if p in chooseList:
                    num += 1
                else: num = 0
        
        return False



    def check_diagonal_line_2(this, chooseList):
        
        start_positions = {}
        tmp = tmp2 = this.n
        tmp3 = this.n # store number position
        start_positions[this.n] = this.n;
        for i in range(this.n-5):
            tmp -= 1
            tmp2 += this.n
            tmp3 -= 1
            start_positions[tmp] = tmp3
            start_positions[tmp2] = tmp3
        
        result = [];   
        for position in start_positions:
            currentPosition = position;
            tmpArr = []
            line_len = start_positions[position]
            for i in range(line_len):
                tmpArr.append(currentPosition);
                currentPosition += (this.n - 1);
            result.append(tmpArr)
        
        num = 0;
        for sub in result:
            num = 0
            for p in sub:
                if num == 5 : return True
                if p in chooseList: num+=1   
                else: num = 0 
        return False

    def check_row(this, chooseList):
        currentPosition = 1;
        result = [];
        for x in range(this.n):
            tmp = [];
            for y in range(this.n):
                tmp.append(currentPosition);
                currentPosition += 1;
            result.append(tmp);
        
        
        for subList in result:
            num = 0;
            for p in subList:
                if num == 5: return True;
                if p in chooseList: num += 1
                else: num = 0
        return False;

    def check_column(this, chooseList):
        result = [];
        col = 1;
        for y in range(this.n):
            
            currentPosition = col;
            tmp = [];
            for x in range(this.n):
                tmp.append(currentPosition);
                currentPosition += this.n;
            col += 1;
            result.append(tmp);
        
        for sub in result:
            num = 0;
            for p in sub:
                if num == 5: return True;
                if p in chooseList: num += 1
                else: num =0
        return False
  


class myApp(QWidget):
    def __init__(this):
        super(myApp, this).__init__()
        
        this.widthWindow = 800
        this.heightWindow = 700
        
        this.widthFrame = 600
        this.heightFrame = 600
        
        this.setFixedSize(this.widthWindow,this.heightWindow)
        this.setWindowTitle("Test UI");
        this.arrResult = [];
        this.arr2D = [];
        this.ticked = [];

        this.playerChoose = [];
        this.botChoose = [];

        
        
        this.initUi();
        this.isPlayer = True;

    def initUi(this):
        this.groupButton = QButtonGroup(this)
        layout = QGridLayout();
        this.frame = QtWidgets.QFrame(this);
        this.frame.setFixedSize(this.widthFrame,this.heightFrame);
        xFrame = (this.widthWindow / 2) - (this.widthFrame / 2)
        this.frame.move(xFrame,50)
        this.lable = QtWidgets.QLabel(this);
        this.lable.setText("Player go first")
        this.lable.setFixedSize(500,50)
        
        index = 1;
        this.n = 10;
        for x in range(this.n):
            for y in range(this.n):
                button = QPushButton("");
                button.setFixedSize(50,50)
                try:
                    button.clicked.connect(this.eventMouse(index));
                except:
                    pass
                this.groupButton.addButton(button, index);
                layout.addWidget(button, x, y);
                index += 1;
        # layout.setHorizontalSpacing(30)
        # layout.setVerticalSpacing(30)
        this.frame.setLayout(layout)
        # this.setLayout(layout);
        this.adjustSize();

    def initWin(this): pass

    def eventMouse(this, id):
        def runEvent():
            # print("Button ID: " + str(id));
            if id in this.ticked:
                return
            if this.isPlayer:
                this.groupButton.button(id).setStyleSheet(
                    "background-color : blue");
                this.groupButton.button(id).setText("X")
                this.playerChoose.append(int(id));
                
                result = this.check_Win(this.playerChoose);
                if result: this.showMessageDialog("Player");
            else:
                this.groupButton.button(id).setStyleSheet(
                    "background-color : red");
                this.groupButton.button(id).setText("O")
                    
                this.botChoose.append(int(id));
                result = this.check_Win(this.botChoose);
                if result: this.showMessageDialog("Bot");
            
            
            this.ticked.append(id);
            this.isPlayer = not this.isPlayer;
        return runEvent;

    def updateComponent(this, ):
        this.label.adjustSize();

    def check_Win(this, listchoose):
        check = CheckWin(this.n);
        check_diagonal_line_1 = check.check_diagonal_line_1(listchoose);
        check_diagonal_line_2 = check.check_diagonal_line_2(listchoose);
        check_row = check.check_row(listchoose);
        check_column = check.check_column(listchoose);
        if check_column or check_row or check_diagonal_line_1 or check_diagonal_line_2 :
            return True;
        return False;
        
    def showMessageDialog(this, player):
        msg_box = QMessageBox() ;
        msg_box.setText(player + " Win!")
        msg_box.setIcon(QMessageBox.Information) 
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_() 

def runMyapp():
    app = QApplication([])
    win = myApp()
    win.show()
    app.exec_()


runMyapp()
