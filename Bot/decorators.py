class InputErrorDecorator:
    @staticmethod
    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "ololo"
            except KeyError:
                return "Contact not found."
            except IndexError:
                return "Invalid index."

        return inner
