from ext import *
import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtPrintSupport
from PyQt5.QtCore import Qt, pyqtSignal, QObject

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent =None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.filename = ""
        self.initUI()
        self.changesSaved = True

    def initToolbar(self):

        tableAction = QtWidgets.QAction(QtGui.QIcon("icons/table.png"),"Insert Table",self)
        tableAction.setStatusTip("Insert Table")
        tableAction.setShortcut("Ctrl+T")
        tableAction.triggered.connect(tables.Table(self).show)

        dateTimeAction = QtWidgets.QAction(QtGui.QIcon("icons/calender.png"),"Insert current date/time",self)
        dateTimeAction.setStatusTip("Insert Current date/time")
        dateTimeAction.setShortcut("Ctrl+D")
        dateTimeAction.triggered.connect(datetime.DateTime(self).show)

        wordCountAction = QtWidgets.QAction(QtGui.QIcon("icons/count.png"),"see word/symbol count", self)
        wordCountAction.setStatusTip("See word/symbol count")
        wordCountAction.setShortcut("Ctrl+W")
        wordCountAction.triggered.connect(self.wordCount)


        imageAction = QtWidgets.QAction(QtGui.QIcon("icons/image.png"),"Insert Image", self)
        imageAction.setStatusTip("Insert Image")
        imageAction.setShortcut("Ctrl+Shift+I")
        imageAction.triggered.connect(self.insertImage)


        self.findAction = QtWidgets.QAction(QtGui.QIcon("icons/find.png"),"Find and Replace", self)
        self.findAction.setStatusTip("Find and Replace words in your document")
        self.findAction.setShortcut("Ctrl + F")
        self.findAction.triggered.connect(find.Find(self).show)

        bulletAction = QtWidgets.QAction(QtGui.QIcon("icons/bullet.png"),"Insert Bullet List", self)
        bulletAction.setStatusTip("Insert Bullet List")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)


        numberedAction = QtWidgets.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered list",self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        self.cutAction = QtWidgets.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard", self)
        self.cutAction.setStatusTip("Cut to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtWidgets.QAction(QtGui.QIcon("icons/copy.png"),"copy to clipboard", self)
        self.copyAction.setStatusTip("copy to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtWidgets.QAction(QtGui.QIcon("icons/paste.png"),"paste to screen", self)
        self.pasteAction.setStatusTip("Paste to screen")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtWidgets.QAction(QtGui.QIcon("icons/undo.png"), "undo action", self)
        self.undoAction.setStatusTip("undo action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtWidgets.QAction(QtGui.QIcon("icons/redo.png"), "redo action", self)
        self.redoAction.setStatusTip("redo action")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        self.printAction = QtWidgets.QAction(QtGui.QIcon("icons/print.png"),"Print Document", self)
        self.printAction.setStatusTip("Print Document")
        self.printAction.setShortcut("Ctrl+ P")
        self.printAction.triggered.connect(self.print)

        self.previewAction = QtWidgets.QAction(QtGui.QIcon("icons/preview.png"),"Preview Document", self)
        self.previewAction.setStatusTip("Preview a document")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.newAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("Create new document from scratch")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"),"open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/save.png"),"save file",self)
        self.saveAction.setStatusTip("Save a written document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)
        self.toolbar.addAction(wordCountAction)
        self.toolbar.addAction(imageAction)
        self.toolbar.addAction(dateTimeAction)
        self.toolbar.addAction(tableAction)



        self.toolbar.addSeparator()

        self.toolbar.addAction(self.findAction)


        self.toolbar.addSeparator()

        self.addToolBarBreak

    def initFormatbar(self):

        indentAction = QtWidgets.QAction(QtGui.QIcon("icons/indent.png"),"Indent Area",self)
        indentAction.setShortcut("Ctrl+Tab")
        indentAction.triggered.connect(self.indent)

        dedentAction = QtWidgets.QAction(QtGui.QIcon("icons/dedent.png"), "dedent Area", self)
        dedentAction.setShortcut("Shift+Tab")
        dedentAction.triggered.connect(self.dedent)



        alignLeft = QtWidgets.QAction(QtGui.QIcon("icons/align-left.png"),"Align Left",self)
        alignLeft.triggered.connect(self.alignLeft)

        alignRight = QtWidgets.QAction(QtGui.QIcon("icons/align-right.png"), "Align Right", self)
        alignRight.triggered.connect(self.alignRight)

        alignCenter = QtWidgets.QAction(QtGui.QIcon("icons/align-center.png"), "Align Center", self)
        alignCenter.triggered.connect(self.alignCenter)

        alignJustify = QtWidgets.QAction(QtGui.QIcon("icons/align-justify.png"), "Align Justify", self)
        alignJustify.triggered.connect(self.alignJustify)

        boldAction =QtWidgets.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtWidgets.QAction(QtGui.QIcon("icons/italic.png"),"Italic", self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtWidgets.QAction(QtGui.QIcon("icons/underline.png"),"Underline", self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QtWidgets.QAction(QtGui.QIcon("icons/strike.png"),"Strikethrough", self)
        strikeAction.triggered.connect(self.strike)

        superAction = QtWidgets.QAction(QtGui.QIcon("icons/superscript.png"),"Superscript", self)
        superAction.triggered.connect(self.superScript)

        subAction = QtWidgets.QAction(QtGui.QIcon("icons/subscript.png"),"Subscript", self)
        subAction.triggered.connect(self.subScript)

        fontBox = QtWidgets.QFontComboBox(self)
        fontBox.currentFontChanged.connect(self.fontFamily)
        fontSize = QtWidgets.QComboBox(self)
        fontSize.setEditable(True)

        #Minimum number of characters displayed

        fontSize.setMinimumContentsLength(3)
        fontSize.activated.connect(self.fontSize)

        fontSizes = ['6','7','8','9','10','11','12','13','14',
             '15','16','18','20','22','24','26','28',
             '32','36','40','44','48','54','60','66',
             '72','80','88','96']

        for i in fontSizes:
            fontSize.addItem(i)

        fontColor = QtWidgets.QAction(QtGui.QIcon("icons/font-color.png"),"change font color", self)
        fontColor.triggered.connect(self.fontColor)

        backColor = QtWidgets.QAction(QtGui.QIcon("icons/highlight.png"),"change background color",self)
        backColor.triggered.connect(self.highlight)

        self.formatbar = self.addToolBar("Format")

        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)
        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)
        self.formatbar.addAction(strikeAction)
        self.formatbar.addAction(superAction)
        self.formatbar.addAction(subAction)
        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)
        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)


        self.formatbar.addSeparator()




    def initMenubar(self):

        toolbarAction = QtWidgets.QAction("Toggle Toolbar",self)
        toolbarAction.triggered.connect(self.toggleToolbar)

        formatbarAction = QtWidgets.QAction("Toggle Formatbar",self)
        formatbarAction.triggered.connect(self.toggleFormatbar)

        statusbarAction = QtWidgets.QAction("Toggle Statusbar",self)
        statusbarAction.triggered.connect(self.toggleStatusbar)

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.findAction)
        view.addAction(toolbarAction)
        view.addAction(formatbarAction)
        view.addAction(statusbarAction)

    def initUI(self):
        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))
        self.text.cursorPositionChanged.connect(self.cursorPosition)
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)
        self.text.textChanged.connect(self.changed)

        self.statusbar = self.statusBar()
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Writer")

    def changed(self):
        self.changesSaved = False

    def closeEvent(self, event):

        if self.changesSaved:

            event.accept()

        else:

            popup = QtWidgets.QMessageBox(self)

            popup.setIcon(QtWidgets.QMessageBox.Warning)

            popup.setText("The document has been modified")

            popup.setInformativeText("Do you want to save your changes?")

            popup.setStandardButtons(QtWidgets.QMessageBox.Save |
                                     QtWidgets.QMessageBox.Cancel |
                                     QtWidgets.QMessageBox.Discard)

            popup.setDefaultButton(QtWidgets.QMessageBox.Save)

            answer = popup.exec_()

            if answer == QtWidgets.QMessageBox.Save:
                self.save()



            elif answer == QtWidgets.QMessageBox.Discard:
                event.accept()

            else:
                event.ignore()

    def context(self,pos):
        #grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table, if there is one
        table = cursor.currentTable()

        # Above will return 0 if there is no current table, in which case
        # we call the normal context menu. If there is a table, we create
        # our own context menu specific to table interaction
        if table:
            menu = QtWidgets.QMenu(self)

            appendRowAction = QtWidgets.QAction("Append Row",self)
            appendRowAction.triggered.connect(lambda :table.appendRows(1))

            appendColAction = QtWidgets.QAction("Append column",self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))

            removeRowAction = QtWidgets.QAction("remove row",self)
            removeRowAction.triggered.connect(self.removeRow)

            removeColAction = QtWidgets.QAction("Remove column", self)
            removeColAction.triggered.connect(self.removeCol)

            insertRowAction = QtWidgets.QAction("Insert row", self)
            insertRowAction.triggered.connect(self.insertRow)

            insertColAction = QtWidgets.QAction("Insert column", self)
            insertColAction.triggered.connect(self.insertCol)

            mergeAction = QtWidgets.QAction("Merge cells", self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

            # Only allow merging if there is a selection
            if not cursor.hasSelection():
                mergeAction.setEnabled(False)

            splitAction = QtWidgets.QAction("Split cells", self)

            cell = table.cellAt(cursor)

            # Only allow splitting if the current cell is larger
            # than a normal cell
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                splitAction.triggered.connect(lambda: table.splitCell(cell.row(), cell.column(), 1, 1))

            else:
                splitAction.setEnabled(False)

            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)

            menu.addSeparator()

            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)

            menu.addSeparator()

            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)

            menu.addSeparator()

            menu.addAction(mergeAction)
            menu.addAction(splitAction)

            # Convert the widget coordinates into global coordinates

            pos = self.mapToGlobal(pos)

            # Add pixels for the tool and formatbars, which are not included
            # in mapToGlobal(), but only if the two are currently visible and
            # not toggled by the user

            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)

            # Move the menu to the new position
            menu.move(pos)

            menu.show()

        else:
            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())
            self.text.contextMenuEvent(event)

    def removeRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's row
        table.removeRows(cell.row(), 1)

    def removeCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's column
        table.removeColumns(cell.column(), 1)

    def insertRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertRows(cell.row(), 1)

    def insertCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertColumns(cell.column(), 1)




    def wordCount(self):
        #print("REACH ESTABLISHED")
        wc = wordcount.WordCount(self)
        wc.getText()
        wc.show()

    def insertImage(self):
        #get a image file name
        print("debug 1")
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'Insert Image',".","Images(*.png *.xpm *.jpg *.bmp *gif)")[0]
        print("debug 2")

        #create image object

        image = QtGui.QImage(filename)
        print("debug 4")
        #Error if unloadable
        if image.isNull():
            print("debug 3")
            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Image Load Error", "Could not load image file!", QtWidgets.QMessageBox.Ok, self)
            popup.show()
        else:
            cursor = self.text.textCursor()
            cursor.insertImage(image,filename)

    def toggleToolbar(self):
        state = self.toolbar.isVisible()
        self.toolbar.setVisible(not state)

    def toggleFormatbar(self):
        state = self.formatbar.isVisible()
        self.formatbar.setVisible(not state)

    def toggleStatusbar(self):
        state = self.statusbar.isVisible()
        self.statusbar.setVisible(not state)

    def indent(self):
        cursor = self.text.textCursor()
        if cursor.hasSelection():
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.selectionEnd())
            diff = cursor.blockNumber() - temp

            for n in range(diff + 1):
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)
                cursor.insertText("\t")
                cursor.movePosition(QtGui.QTextCursor.Up)

        else:
            cursor.insertText("\t")

    def dedent(self):
        cursor = self.text.textCursor()
        if cursor.hasSelection():
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.selectionEnd())
            diff = cursor.blockNumber() - temp

            for n in range(diff + 1):
                self.handleDedent(cursor)
                cursor.movePosition(QtGui.QTextCursor.Up)
        else:
            self.handleDedent(cursor)

    def handleDedent(self,cursor):
        cursor.movePosition(QtGui.QTextCursor.StartOfLine)
        line = cursor.block().text()
        if line.startswith("\t"):
            cursor.deleteChar()
        else:
            for char in line[:8]:
                if char !=" ":
                    break

                cursor.deleteChar()

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def bold(self):
        if self.text.fontWeight() == QtGui.QFont.Bold:
            self.text.setFontWeight(QtGui.QFont.Normal)
        else:
            self.text.setFontWeight(QtGui.QFont.Bold)

    def italic(self):
        state = self.text.fontItalic()
        self.text.setFontItalic(not state)

    def underline(self):
        state = self.text.fontUnderline()
        self.text.setFontUnderline(not state)

    def strike(self):
        fmt = self.text.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.text.setCurrentCharFormat(fmt)

    def superScript(self):
        fmt = self.text.currentCharFormat()
        align = fmt.verticalAlignment()

        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

    def subScript(self):
        fmt = self.text.currentCharFormat()
        align = fmt.verticalAlignment()

        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.text.setCurrentCharFormat(fmt)

    def fontFamily(self, font):
        self.text.setCurrentFont(font)

    def fontSize(self, fontsize):
        self.text.setFontPointSize(int(fontsize))

    def fontColor(self):
        color = QtWidgets.QColorDialog.getColor()
        self.text.setTextColor(color)

    def highlight(self):
        color = QtWidgets.QColorDialog.getColor()
        self.text.setTextBackgroundColor(color)


    def cursorPosition(self):
        cursor = self.text.textCursor()
        line = cursor.blockNumber()+1
        col = cursor.columnNumber()
        self.statusBar().showMessage("Line {} | Column : {}".format(line,col))

    def bulletList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):
        cursor = self.text.textCursor()

        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def preview(self):
        preview = QtPrintSupport.QPrintPreviewDialog()
        preview.paintRequested.connect(lambda p: self.text.print_(p))
        preview.exec_()

    def print(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def new(self):
        spawn = Main(self)
        spawn.show()

    def open(self):

        self.filename = QtWidgets.QFileDialog.getOpenFileName(self,'open file',".","(*.writer)")[0]

        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())


    def save(self):
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self,'save file')[0]

        if not self.filename.endswith(".writer"):
            self.filename += ".writer"


        with open(self.filename,"wt") as file:
            file.write(self.text.toHtml())

        self.changesSaved = True






def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

