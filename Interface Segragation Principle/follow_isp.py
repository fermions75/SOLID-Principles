from abc import ABC, abstractmethod

class ViewContentInterface(ABC):
    @abstractmethod
    def view_content(self):
        pass


class EditContentInterface(ABC):
    @abstractmethod
    def edit_content(self):
        pass


class DeleteContentInterface(ABC):
    @abstractmethod
    def delete_content(self):
        pass


class RegularUser(ViewContentInterface):
    def view_content(self):
        print("Viewing content")


class AdminUser(ViewContentInterface, EditContentInterface, DeleteContentInterface):
    def view_content(self):
        print("Viewing content")

    def edit_content(self):
        print("Editing content")

    def delete_content(self):
        print("Deleting content")

# Usage
regular_user = RegularUser()
regular_user.view_content()  # Works fine

admin_user = AdminUser()
admin_user.edit_content()    # Works fine for admin
admin_user.delete_content()  # Works fine for admin

"""
The RegularUser class now only implements the methods it needs, adhering to the Interface Segregation Principle.
"""