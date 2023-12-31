# Import necessary packages here
from typing import List

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtWidgets import (
    QButtonGroup,
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QShortcut,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from todo_five.database import ToDoDatabase

# ==========================================================================================
# ==========================================================================================

# File:    widgets.py
# Date:    June 01, 2023
# Author:  Jonathan A. Webb
# Purpose: This file contains classes that implement widgets to be used in the todo_six
#          code base.  In most cases the classes act as wrappers around widgets
#          implemented in the PyQt5 library.
# ==========================================================================================
# ==========================================================================================
# Insert Code here


class DayNightRadioButton(QWidget):
    """
    Custom QWidget that contains two QRadioButtons for selecting Day or Night themes.

    :param active_widget: Widget is active when created if set to True, inactive
                          if set to false
    """

    def __init__(self, active_widget: bool = True):
        super().__init__()

        self.form = QHBoxLayout(self)
        self.button_group = QButtonGroup(self)

        self.day_button = QRadioButton("Day")
        self.night_button = QRadioButton("Night")

        self.form.addWidget(self.day_button)
        self.form.addWidget(self.night_button)

        self.button_group.addButton(self.day_button)
        self.button_group.addButton(self.night_button)

        # Set the day theme as default
        self.day_button.setChecked(True)
        self.setEnabled(active_widget)


# ==========================================================================================
# ==========================================================================================


class DropDownMenu(QComboBox):
    """
    Class to create a drop-down menu

    :param options: A list of text strings describing possible options for the
    drop-down menu

    :param active_widget: Widget is active when created if set to True, inactive
                          if set to false
    """

    def __init__(self, options: List[str], active_widget: bool = True):
        super().__init__()
        self.addItems(options)
        self.setCurrentIndex(0)  # Set default selection to the first item
        self.setEnabled(active_widget)

    # ------------------------------------------------------------------------------------------

    def get_selected_option(self) -> str:
        """
        Method to return the selected option

        :return option: The selected option as a string
        """
        return self.currentText()

    # ------------------------------------------------------------------------------------------

    def set_selected_option(self, option: str) -> None:
        """
        Method that allows a user to enter an option as a text string

        :param option: A text string describing the option
        """
        index = self.findText(option)
        if index >= 0:
            self.setCurrentIndex(index)


# ==========================================================================================
# ==========================================================================================


class LineEdit(QLineEdit):
    """
    Custom QLineEdit with specific text and font

    :param font: A QFont object with font type and font size
    :param active_widget: Widget is active when created if set to True, inactive
                          if set to false
    """

    def __init__(self, font: QFont, active_widget: bool = True):
        super().__init__()
        self.setFont(font)
        self.setEnabled(active_widget)

    # ------------------------------------------------------------------------------------------

    def set_text(self, text: str) -> None:
        """
        Method to set the text in the QLineEdit

        :param text: The text to be set
        """
        self.setText(text)

    # ------------------------------------------------------------------------------------------

    def get_text(self) -> str:
        """
        Method to get the text in the QLineEdit

        :return: The text in the QLineEdit
        """
        return self.text()


# ==========================================================================================
# ==========================================================================================


class ListWidget(QListWidget):
    """
    Custom QListWidget with specific text and font

    :param font: A QFont object with font type and font size
    :param active_widget: Widget is active when created if set to True, inactive
                          if set to false
    """

    def __init__(self, font: QFont, active_widget: bool = True):
        super().__init__()
        self.setFont(font)
        self.setEnabled(active_widget)

    # ------------------------------------------------------------------------------------------

    def add_item(self, item: str) -> None:
        """
        Method to add an item to the QListWidget

        :param item: The item to be added
        """
        self.addItem(item)

    # ------------------------------------------------------------------------------------------

    def remove_item(self, item: str) -> None:
        """
        Method to remove an item from the QListWidget

        :param item: The item to be removed
        """
        items = self.findItems(item, Qt.MatchExactly)
        if not items:
            return  # No item found to be removed
        for item in items:
            self.takeItem(self.row(item))

    # ------------------------------------------------------------------------------------------

    def get_selected_item(self) -> str:
        """
        Method to get the currently selected item in the QListWidget

        :return: The currently selected item
        """
        return self.currentItem().text() if self.currentItem() else None


# ==========================================================================================
# ==========================================================================================


class OpacitySlider(QWidget):
    """
    Custom QWidget that contains a QLabel and a QSlider for setting the opacity.

    :param active_widget: Widget is active when created if set to True, inactive
                          if set to false
    """

    def __init__(self, active_widget: bool = True):
        super().__init__()

        # Create a QHBoxLayout
        layout = QHBoxLayout()

        # Create a QLabel with a default opacity of 100
        self.label = QLabel("Opacity: 100")

        # Create a QSlider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)  # Opacity range from 0% to 100%
        self.slider.setValue(100)  # Default opacity is 100%

        # Connect slider's value change signal to update_label function
        self.slider.valueChanged.connect(self.update_label)

        # Add the QLabel and QSlider to the QHBoxLayout
        layout.addWidget(self.label)
        layout.addWidget(self.slider)

        # Set the QHBoxLayout as the layout for this widget
        self.setLayout(layout)
        self.setEnabled(active_widget)

    # ------------------------------------------------------------------------------------------

    def update_label(self, value: int) -> None:
        """
        Updates the QLabel text with the current slider value.

        :param value: The current value of the slider.
        """
        # Update the label text with the new slider value
        self.label.setText(f"Opacity: {value}")

    # ------------------------------------------------------------------------------------------

    def set_opacity(self, value: int) -> None:
        """
        Method to set the opacity

        :param value: The opacity value to be set
        """
        self.slider.setValue(value)

    # ------------------------------------------------------------------------------------------

    def get_opacity(self) -> int:
        """
        Method to get the current opacity value

        :return: The current opacity value
        """
        return self.slider.value()


# ==========================================================================================
# ==========================================================================================


class PushButton(QPushButton):
    """
    Custom QPushButton with specific text and font.

    :param text: The text to be displayed on a button
    :param font: A QFont object with font type and font size
    :param active_widget: Widget is active when created if set to True, inactive
                          if set to false
    """

    def __init__(self, text: str, font: QFont, active_widget: bool = True):
        super().__init__(text)
        self.setFont(font)
        self.setEnabled(active_widget)


# ==========================================================================================
# ==========================================================================================


class Tab(QWidget):
    """
    Class to set a tab instantiation for the todo_six application.

    :param fnt: A QFont object
    :param tab_name: A string character name for the object
    :param db: A ToDoDatabase object
    """

    def __init__(self, fnt: QFont, tab_name: str, db: ToDoDatabase):
        super().__init__()
        self.tab_name = tab_name
        self.tab_layout = QVBoxLayout(self)
        self.db = db

        success, oldest_date, _ = self.db.get_oldest_date()
        if not success:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Failed to query the oldest date.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        # Convert the oldest_date and today's date to QDate objects
        if oldest_date:
            start_date = QDate.fromString(oldest_date, "yyyy-MM-dd")
        else:
            start_date = QDate.currentDate()
        end_date = QDate.currentDate()

        self.widgets = {
            "entry_field": QLineEdit(),
            "todo_list": QListWidget(),
            "todo_list_label": QLabel("Todo List"),
            "completed_list_label": QLabel("Completed List"),
            "completed_list": QListWidget(),
            "add_task_button": QPushButton("Add Task"),
            "retire_task_button": QPushButton("Retire Task"),
            "delete_task_button": QPushButton("Delete Task"),
            "drop_down_menu": DropDownMenu(["Day", "Week", "Month", "Year", "All"]),
            "calendar": QDateEdit(),
        }

        self.widgets["entry_field"].setFont(fnt)
        self.widgets["todo_list"].setFont(fnt)
        self.widgets["todo_list_label"].setFont(fnt)
        self.widgets["completed_list_label"].setFont(fnt)
        self.widgets["completed_list"].setFont(fnt)
        self.widgets["add_task_button"].setFont(fnt)
        self.widgets["retire_task_button"].setFont(fnt)
        self.widgets["delete_task_button"].setFont(fnt)
        self.widgets["drop_down_menu"].setFont(fnt)

        self.tab_layout.addWidget(self.widgets["entry_field"])
        self.tab_layout.addWidget(self.widgets["todo_list_label"])
        self.tab_layout.addWidget(self.widgets["todo_list"])
        self.tab_layout.addWidget(self.widgets["completed_list_label"])
        self.tab_layout.addWidget(self.widgets["completed_list"])
        self.tab_layout.addWidget(self.widgets["add_task_button"])
        self.tab_layout.addWidget(self.widgets["retire_task_button"])
        self.tab_layout.addWidget(self.widgets["delete_task_button"])

        self.widgets["add_task_button"].clicked.connect(self._add_task)
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.shortcut.activated.connect(self._add_task)

        self.widgets["retire_task_button"].clicked.connect(self._retire_task)
        self.shortcut = QShortcut(QKeySequence(Qt.Key_Delete), self)
        self.shortcut.activated.connect(self._retire_task)

        self.widgets["delete_task_button"].clicked.connect(self._delete_task)
        self.delete_all_shortcut = QShortcut(QKeySequence("Shift+Delete"), self)
        self.delete_all_shortcut.activated.connect(self._delete_task)

        self.widgets["drop_down_menu"].currentTextChanged.connect(
            self._update_completed_tasks
        )

        self.widgets["todo_list"].itemSelectionChanged.connect(
            self._clear_other_selections
        )
        self.widgets["completed_list"].itemSelectionChanged.connect(
            self._clear_other_selections
        )
        self.delete_mode = False

        self.todo_tasks = {}
        self.completed_tasks = {}

        self._load_tasks_from_database()

        self.widgets["calendar"].setCalendarPopup(True)
        # Set minimum and maximum dates
        self.widgets["calendar"].setMinimumDate(start_date)
        self.widgets["calendar"].setMaximumDate(end_date)
        self.widgets["calendar"].setDate(QDate.currentDate())

        # Create a QHBoxLayout
        final_row_layout = QHBoxLayout()

        # Add drop_down_menu and calendar to the QHBoxLayout
        final_row_layout.addWidget(self.widgets["drop_down_menu"])
        final_row_layout.addWidget(self.widgets["calendar"])

        # Add the QHBoxLayout to the main layout
        self.tab_layout.addLayout(final_row_layout)

        # Create connections for calendar
        self.widgets["calendar"].dateChanged.connect(self._date_changed)

    # ------------------------------------------------------------------------------------------

    def _load_tasks_from_database(self):
        """
        A method to load tasks from the database. The tasks will be added to the
        appropriate task list and also to the corresponding task dictionary.
        """

        # Query the database for open tasks
        self._refresh_tasks()

    # ------------------------------------------------------------------------------------------

    def _add_task(self):
        """
        Method to add a task to the todo_list window of the appropriate tab
        """
        task_text = self.widgets["entry_field"].text()
        if task_text:
            success, message, task_id = self.db.insert_task(task_text)
            if not success:
                # Display a message box if there's an error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Error")
                msg.setInformativeText(message)
                msg.setWindowTitle("Error")
                msg.exec()
                return
            # Get the last inserted id from the database
            last_id = self._get_largest_id_in_todo_list()
            new_id = last_id + 1
            self.widgets["todo_list"].addItem(f"{new_id}. {task_text}")
            self.todo_tasks[new_id] = task_id
            self.widgets["entry_field"].setText("")  # clear the entry field

    # ------------------------------------------------------------------------------------------

    def _get_largest_id_in_todo_list(self) -> int:
        """
        Return the largest ID currently in the todo_list.
        """
        max_id = 0
        for i in range(self.widgets["todo_list"].count()):
            item_text = self.widgets["todo_list"].item(i).text()
            item_id = int(
                item_text.split(".")[0]
            )  # assuming item_text is in "id: text" format
            if item_id > max_id:
                max_id = item_id
        return max_id

    # ------------------------------------------------------------------------------------------

    def _retire_task(self) -> None:
        """
        Method to retire a task from the todo_list window of the appropriate tab
        """
        # 1. Retire the selected task
        current_task = self.widgets["todo_list"].currentItem()
        if not current_task:
            return  # If no item selected, do nothing
        task_id, _ = current_task.text().split(". ", 1)
        db_task_id = self.todo_tasks[int(task_id)]
        success, message = self.db.complete_task(db_task_id)
        if not success:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Error")
            msg.setInformativeText(message)
            msg.setWindowTitle("Error")
            msg.exec()
            return

        # 4. Remove the updated task from the todo list
        self.widgets["todo_list"].takeItem(self.widgets["todo_list"].row(current_task))
        del self.todo_tasks[int(task_id)]  # remove from our tracking dictionary

        # 2. Clear the completed list
        self.widgets["completed_list"].clear()

        # 3. Query the database for completed tasks
        if success:
            self._refresh_tasks()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Error")
            msg.setInformativeText(message)
            msg.setWindowTitle("Error")
            msg.exec()

    # ------------------------------------------------------------------------------------------

    def _clear_other_selections(self):
        """
        Method to ensure that only one task can be highlighted at a time.
        """
        if not self.delete_mode:  # Skip clearing if we're in delete mode
            sender = self.sender()
            if sender is self.widgets["todo_list"]:
                self.widgets["completed_list"].clearSelection()
        else:
            self.widgets["todo_list"].clearSelection()

    # ------------------------------------------------------------------------------------------

    def _delete_task(self) -> None:
        """
        Method to delete the selected task from the database and the respective list
        window.
        """
        # 1. Determine which list the user is interacting with
        selected_list = None
        selected_item = None
        task_dict = None
        if self.widgets["todo_list"].selectedItems():
            selected_list = self.widgets["todo_list"]
            selected_item = selected_list.currentItem()
            task_dict = self.todo_tasks
        elif self.widgets["completed_list"].selectedItems():
            selected_list = self.widgets["completed_list"]
            selected_item = selected_list.currentItem()
            task_dict = self.completed_tasks

        if selected_item is None:
            QMessageBox.warning(self, "Error", "No task selected.")
            return

        # 2. Determine the task id
        task_id, _ = selected_item.text().split(". ", 1)
        db_task_id = task_dict[int(task_id)]

        # 3. Confirmation window
        confirm = QMessageBox.question(
            self,
            "Confirm Deletion",
            "Are you sure you want to delete the selected task?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        # 4. Delete the task from the database
        if confirm == QMessageBox.StandardButton.Yes:
            success, message = self.db.delete_task(db_task_id)
            if not success:
                QMessageBox.warning(self, "Error", f"Failed to delete task: {message}")
                return

            # 5. Refresh the tasks
            self._refresh_tasks()

    # ------------------------------------------------------------------------------------------

    def _update_completed_tasks(self):
        """
        Method to refresh the completed tasks list based on the selected time frame
        from the drop_down_menu.
        """
        time_frame = self.widgets["drop_down_menu"].currentText().upper()
        # Get selected date from the QDateEdit widget
        selected_date = self.widgets["calendar"].date().toString("yyyy-MM-dd")
        success, df, message = self.db.select_closed_tasks(time_frame, selected_date)
        if success:
            self._populate_tasks(df, self.widgets["completed_list"], self.completed_tasks)
        else:
            msg = f"Failed to query completed tasks: {message}"
            QMessageBox.warning(self, "Error", msg)

    # ------------------------------------------------------------------------------------------

    def _refresh_tasks(self):
        """
        Method to refresh the tasks from the database.
        """
        # Refresh the todo tasks
        success, df, message = self.db.select_open_tasks()
        if success:
            self._populate_tasks(df, self.widgets["todo_list"], self.todo_tasks)
        else:
            QMessageBox.warning(self, "Error", f"Failed to query open tasks: {message}")

        # Refresh the completed tasks
        time_frame = self.widgets["drop_down_menu"].currentText().upper()
        success, df, message = self.db.select_closed_tasks(time_frame)
        if success:
            self._populate_tasks(df, self.widgets["completed_list"], self.completed_tasks)
        else:
            QMessageBox.warning(
                self, "Error", f"Failed to query completed tasks: {message}"
            )

    # ------------------------------------------------------------------------------------------

    def _populate_tasks(self, df, list_widget, task_dict):
        """
        Method to populate a list widget with tasks from a DataFrame and update a
        corresponding task dictionary.
        """
        list_widget.clear()
        task_dict.clear()
        for idx, row in enumerate(df.iterrows(), start=1):
            task_id = row[1]["task_id"]
            task = row[1]["task"]
            list_widget.addItem(f"{idx}. {task}")
            task_dict[idx] = task_id

    # ------------------------------------------------------------------------------------------

    def _date_changed(self, qdate):
        """
        Method to update the task lists based on the selected date from the calendar
        widget.
        """
        # Convert the QDate object to a string
        selected_date = qdate.toString("yyyy-MM-dd")
        current_date = QDate.currentDate().toString("yyyy-MM-dd")

        if selected_date == current_date:
            # Re-enable buttons and entry field if it's current date
            self.widgets["entry_field"].setEnabled(True)
            self.widgets["add_task_button"].setEnabled(True)
            self.widgets["retire_task_button"].setEnabled(True)
            self.widgets["delete_task_button"].setEnabled(True)
            # Refresh tasks
            self._refresh_tasks()
        else:
            # Disable buttons and entry field if it's not current date
            self.widgets["entry_field"].setEnabled(False)
            self.widgets["add_task_button"].setEnabled(False)
            self.widgets["retire_task_button"].setEnabled(False)
            self.widgets["delete_task_button"].setEnabled(False)
            # Get tasks from selected date
            success, open_tasks, message = self.db.get_former_open_tasks(selected_date)
            if success:
                self._populate_tasks(
                    open_tasks, self.widgets["todo_list"], self.todo_tasks
                )
            else:
                QMessageBox.warning(
                    self, "Error", f"Failed to query open tasks: {message}"
                )

            time_frame = self.widgets["drop_down_menu"].currentText().upper()
            success, closed_tasks, _ = self.db.select_closed_tasks(
                time_frame, selected_date
            )
            if success:
                self._populate_tasks(
                    closed_tasks, self.widgets["completed_list"], self.completed_tasks
                )
            else:
                QMessageBox.warning(
                    self, "Error", f"Failed to query completed tasks: {message}"
                )


# ==========================================================================================
# ==========================================================================================
# eof
