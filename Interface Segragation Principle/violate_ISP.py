from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def view_content(self):
        pass

    @abstractmethod
    def edit_content(self):
        pass

    @abstractmethod
    def delete_content(self):
        pass

class RegularUser(UserInterface):
    def view_content(self):
        print("Viewing content")

    def edit_content(self):
        raise NotImplementedError("Regular users cannot edit content")

    def delete_content(self):
        raise NotImplementedError("Regular users cannot delete content")

class AdminUser(UserInterface):
    def view_content(self):
        print("Viewing content")

    def edit_content(self):
        print("Editing content")

    def delete_content(self):
        print("Deleting content")

# Usage
regular_user = RegularUser()
regular_user.view_content()  # Works fine
# regular_user.edit_content()  # Raises NotImplementedError

"""
In this scenario, the RegularUser class is forced to implement methods it does not need, leading to unnecessary code and potential errors. This violates the Interface Segregation Principle.
Adhering to ISP
"""
