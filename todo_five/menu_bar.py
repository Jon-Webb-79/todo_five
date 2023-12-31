from PyQt5.QtWidgets import QAction, QMenu, QMenuBar

# ==========================================================================================
# ==========================================================================================

# File:    menu_bar.py
# Date:    June 07, 2023
# Author:  Jonathan A. Webb
# Purpose: This file contains all classes and functions necessary to run the file menu
#          for the todo_six application
# ==========================================================================================
# ==========================================================================================
# Insert Code here


class FileMenu:
    """
    Class that builds all functionality necessary to implement the File attributes
    of the menu bar

    :param controller: A ToDoListController object
    """

    def __init__(self, create_db_func, open_db_func, close_db_func):
        self.create_db_func = create_db_func
        self.open_db_func = open_db_func
        self.close_db_func = close_db_func
        self.menu = QMenu("File")
        self._create_actions()
        self._add_actions()

    # ------------------------------------------------------------------------------------------

    def open_db(self):
        """
        Method that encodes the functionality of the Open attribute
        """
        self.open_db_func()
        print("Opened Database")

    # ------------------------------------------------------------------------------------------

    def new_db(self):
        """
        Method that encodes the functionality of the New attribute
        """
        self.create_db_func()
        print("Created New Database")

    # ------------------------------------------------------------------------------------------

    def close_db(self):
        """
        Method that encodes the functionality of the Close attribute
        """
        self.close_db_func()
        print("Closed databases")

    # ==========================================================================================
    # PRIVATE LIKE METHODS

    def _create_actions(self):
        """
        Creates and connects slots for attributes of the File menu bar item
        """
        self.open_action = QAction("Open")
        self.new_action = QAction("New")
        self.close_action = QAction("Close")

        # Connect actions to slots
        self.open_action.triggered.connect(self.open_db)
        self.new_action.triggered.connect(self.new_db)
        self.close_action.triggered.connect(self.close_db)

    # ------------------------------------------------------------------------------------------

    def _add_actions(self):
        """
        Adds slots for the File menu bar item
        """
        self.menu.addAction(self.open_action)
        self.menu.addAction(self.new_action)
        self.menu.addAction(self.close_action)


# ==========================================================================================
# ==========================================================================================


class MenuBar(QMenuBar):
    """
    Custom implementation of the QMenuBar item.  This class integrates all menu
    bar classes into one implementation

    :param controller: A ToDoListController object
    """

    def __init__(self, create_db_func, open_db_func, close_db_func):
        super().__init__()

        self.file_menu = FileMenu(create_db_func, open_db_func, close_db_func)

        self.addMenu(self.file_menu.menu)


# ==========================================================================================
# ==========================================================================================
# eof
