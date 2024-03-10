

class InputErrorDecorator:
    @staticmethod
    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Error: Invalid input detected."
            except KeyError:
                return "Contact not found."
            except IndexError:
                return "Invalid index."
            except AttributeError:
                return "Attribute error. Please check your input and try again."

        return inner
