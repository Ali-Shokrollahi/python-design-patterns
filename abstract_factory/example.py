"""
Task:
    - You are designing a GUI application that can use either Windows or MacOS styles for its interface components,
     such as buttons and checkboxes.
"""

from abc import ABC, abstractmethod


class Button(ABC):  # Abstract Product
    @abstractmethod
    def click(self):
        ...


class Checkbox(ABC):  # Abstract Product
    @abstractmethod
    def set_checked(self):
        ...


class WindowsButton(Button):  # Concrete Product
    def click(self):
        return "windows button click event triggered"


class MacButton(Button):  # Concrete Product
    def click(self):
        return "mac button click event triggered"


class WindowsCheckbox(Checkbox):  # Concrete Product
    def set_checked(self):
        return "windows checkbox set_checked event triggered"


class MacCheckbox(Checkbox):  # Concrete Product
    def set_checked(self):
        return "mac checkbox set_checked event triggered"


class UiStyleFactory(ABC):
    @abstractmethod
    def create_button(self):
        ...

    @abstractmethod
    def create_checkbox(self):
        ...


class WindowsUiStyleFactory(UiStyleFactory):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacUiStyleFactory(UiStyleFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def read_os_type(types: list) -> str:
    """Read the OS type from user input."""
    while True:
        os_type_input = input("Enter a OS type(windows, mac): ")
        if os_type_input in types:
            return os_type_input
        print("That's not a valid OS type.")


def main(factory: UiStyleFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.set_checked())


if __name__ == '__main__':
    factories = {
        "windows": WindowsUiStyleFactory(),
        "mac": MacUiStyleFactory(),
    }
    main(factories[read_os_type(list(factories.keys()))])
