from PyQt5 import QtGui, QtWidgets, QtCore

from PyQt5.QtCore import Qt

import re

class Find(QtWidgets.QDialog):
    def __init__(self,parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.parent = parent
        self.lastMatch = None
        self.initUI()

    def initUI(self):

        # button to search the document for something
        findButton = QtWidgets.QPushButton("Find", self)
        findButton.clicked.connect(self.find)

        #button to replace last find
        replaceButton = QtWidgets.QPushButton("Replace", self)
        replaceButton.clicked.connect(self.replace)

        #button to remove all findings
        allButton = QtWidgets.QPushButton("Replace All",self)
        allButton.clicked.connect(self.replaceAll)

        #Normal mode radio button
        self.normalRadio = QtWidgets.QRadioButton("Normal", self)
        self.normalRadio.toggled.connect(self.normalMode)

        #Regular expression mode radio button
        self.regexRadio = QtWidgets.QRadioButton("RegEx",self)
        self.regexRadio.toggled.connect(self.regexMode)

        #field into which to find the query
        self.findField = QtWidgets.QTextEdit(self)
        self.findField.resize(250,50)

        #field to type the replacement text

        self.replaceField = QtWidgets.QTextEdit(self)
        self.replaceField.resize(250,50)

        optionsLabel = QtWidgets.QLabel("Options :",self)

        #case sensitivity options
        self.caseSens = QtWidgets.QCheckBox("case sensitive",self)

        #whole words option
        self.wholeWords = QtWidgets.QCheckBox("Whole words",self)

        #layout the objects on screen
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.findField,1,0,1,4)
        layout.addWidget(self.normalRadio, 2, 2)
        layout.addWidget(self.regexRadio, 2, 3)
        layout.addWidget(findButton, 2, 0, 1, 2)
        layout.addWidget(self.replaceField, 3, 0, 1, 4)
        layout.addWidget(replaceButton, 4, 0, 1, 1)
        layout.addWidget(allButton, 4, 2, 1, 2)

        #add some spacing
        spacer = QtWidgets.QWidget(self)
        spacer.setFixedSize(0,10)
        layout.addWidget(spacer,5,0)
        layout.addWidget(optionsLabel, 6, 0)
        layout.addWidget(self.caseSens, 6, 1)
        layout.addWidget(self.wholeWords, 6, 2)

        self.setGeometry(300,300,360,250)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

        # default normal activated

        self.normalRadio.setChecked(True)

    def find(self):

        # grab parent's text
        text = self.parent.text.toPlaintext()

        # the text to search
        query = self.findField.toPlainText()

        #if whole words is checked, we need to append and prepend a non-alphanumeric character

        if self.wholeWords.isChecked():
            query = r'\W' + query + r'\W'
        #by default regex are case sensitive but a search function is not

        flags = 0 if self.caseSens.isChecked() else re.I

        #compile the pattern

        pattern = re.compile(query,flags)

        # if the last search was successful start at the position after the last else start at zero
        start = self.lastMatch.start() + 1 if self.lastMatch else 0

        # the actual search

        self.lastMatch = pattern.search(text,start)
        if self.lastMatch:
            start = self.lastMatch.start()
            end = self.lastMatch.end()

            # If 'Whole words' is checked, the selection would include the two
            # non-alphanumeric characters we included in the search, which need
            # to be removed before marking them.

            if self.wholeWords.isChecked():
                start +=1
                end -= 1

            self.moveCursor(start,end)

        else:
            # We set the cursor to the end if the search was unsuccessful
            self.parent.text.moveCursor(QtGui.QTextCursor.End)

    def replace(self):
        # grab the text cursor
        cursor = self.parent.text.textCursor()
        #security
        if self.lastMatch and cursor.hasSelection():
            # We insert the new text, which will override the selected
            # text
            cursor.insertText(self.replaceField.toPlainText())
            #and set the new cursor
            self.parent.text.setTextCursor()

    def replaceAll(self):
        # Set lastMatch to None so that the search
        # starts from the beginning of the document
        self.lastMatch = None

        # Initial find() call so that lastMatch is
        # potentially not None anymore

        self.find()

        #replace and find until find is none again

        while self.lastMatch:
            self.replace()
            self.find()

    def regexMode(self):
        # uncheck the checkboxes
        self.caseSens.setChecked(False)
        self.wholeWords.setChecked(False)
        # disable them (gray out)
        self.caseSens.setEnabled(False)
        self.wholeWords.setEnabled(False)

    def normalMode(self):
        #enable checkboxes (un-gray them)

        self.caseSens.setEnabled(True)
        self.wholeWords.setEnabled(True)

    def moveCursor(self,start,end):

        # We retrieve the QTextCursor object from the parent's QTextEdit
        cursor = self.parent.text.textCursor()
        # Then we set the position to the beginning of the last match
        cursor.setPosition(start)

        # Next we move the Cursor by over the match and pass the KeepAnchor parameter
        # which will make the cursor select the the match's text

        cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, end - start)
        # And finally we set this new cursor as the parent's
        self.parent.text.setTextCursor(cursor)





