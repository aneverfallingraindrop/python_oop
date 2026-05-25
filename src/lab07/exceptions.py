# custom exceptions baby!

class AppError(Exception):
    # base class for future errors basically a template
    ...

class ItemNotFoundError(AppError):
    # bro who doesnt exist
    ...

class DuplicateItemError(AppError):
    # raised for duplicate student
    ...


class InvalidStudentTypeError(AppError):
    #unknown student types
    ...

class StorageError(AppError):
    # write/read fails 
    ...
