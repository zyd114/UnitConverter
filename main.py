from PySide6.QtWidgets import QApplication, QWidget
from Ui_单位转换器 import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 存储单位和单位大小的字典(映射)
        self.lengthVar = {'千米':1000000, '米':1000, '分米':100, '厘米':10, '毫米':1, '英里':1609344, '英尺': 304.8, '英寸': 25.4}
        self.weightVar = {'千克':1000, '斤':500, '克':1, '吨':1000000}
        
        # 从单位类型到单位字典的映射
        self.typeDict = {'长度': self.lengthVar, '质量': self.weightVar}

        # 给ComboBox组件添加各个选项
        self.dataTypeComboBox.addItems(self.typeDict.keys())
        # 默认输入的是长度单位，后续可以变动
        self.inputTypeComboBox1.addItems(self.lengthVar.keys())
        self.inputTypeComboBox2.addItems(self.lengthVar.keys())
        self.bind()
        # 将初始状态设为 1千米 = 1千米
        self.inputDataEditLine1.setText('1')    # 由于已经bind，所以会直接触发calcUp
    def bind(self):
        self.dataTypeComboBox.currentTextChanged.connect(self.changeDataType)
        # 如果是数据输入框更改，就根据修改的框，计算另一个框更新后的数值
        self.inputDataEditLine1.textChanged.connect(self.calcByUp)
        self.inputDataEditLine2.textChanged.connect(self.calcByDown)
        # 如果是单位更改，就保持上方数值不变，计算下方更新后数值
        self.inputTypeComboBox1.currentTextChanged.connect(self.calcByUp)
        self.inputTypeComboBox2.currentTextChanged.connect(self.calcByUp)

    def calcByUp(self):
        # 获取第一个输入框的值
        value = self.inputDataEditLine1.text()
        if value == '':
            return
        # 获取当前单位和转换单位
        dataType = self.dataTypeComboBox.currentText()
        currentUnit = self.inputTypeComboBox1.currentText()
        transUnit = self.inputTypeComboBox2.currentText()

        # 在转换单位类型的时候会清空单位类型，所以要判断一下单位非空
        if currentUnit == '' or transUnit == '':
            return
        
        # 为了防止信号递归调用，需要临时禁止信号发射
        self.inputDataEditLine2.blockSignals(True)

        # 计算转换后结果
        result = float(value) * self.typeDict[dataType][currentUnit] \
                              / self.typeDict[dataType][transUnit]
        # 限制最大长度为10
        result = f'{result:.10g}'

        # 将结果写入上方label栏和另一个输入框
        self.originDataLabel.setText(f'{value} {currentUnit} = ')
        self.transDataLabel.setText(f'{result} {transUnit}')
        self.inputDataEditLine2.setText(str(result))

        # 恢复信号发射
        self.inputDataEditLine2.blockSignals(False)

    def calcByDown(self):
        # 获取第二个输入框的值
        value = self.inputDataEditLine2.text()
        if value == '':
            return
        # 获取当前单位和转换单位
        dataType = self.dataTypeComboBox.currentText()
        currentUnit = self.inputTypeComboBox2.currentText()
        transUnit = self.inputTypeComboBox1.currentText()

        # 在转换单位类型的时候会清空单位类型，所以要判断一下单位非空
        if currentUnit == '' or transUnit == '':
            return
        
        # 为了防止信号递归调用，需要临时禁止信号发射
        self.inputDataEditLine1.blockSignals(True)

        # 计算转换后结果
        result = float(value) * self.typeDict[dataType][currentUnit] \
                              / self.typeDict[dataType][transUnit]
        # 限制最大长度为10
        result = f'{result:.10g}'

        # 将结果写入上方label栏和另一个输入框
        self.transDataLabel.setText(f'{value} {currentUnit}')
        self.originDataLabel.setText(f'{result} {transUnit} = ')
        self.inputDataEditLine1.setText(str(result))
    
        # 恢复信号发射
        self.inputDataEditLine1.blockSignals(False)

    def changeDataType(self, text):
        # 把ComboBox的选项替换成新类型的单位
        self.inputTypeComboBox1.clear()
        self.inputTypeComboBox2.clear()
        self.inputTypeComboBox1.addItems(self.typeDict[text].keys())
        self.inputTypeComboBox2.addItems(self.typeDict[text].keys())
        # 把输入框重置成初始值
        self.inputDataEditLine1.setText('1')    # 已经bind，所以会自动触发calc
if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()