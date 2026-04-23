

def collection_validate_init(self, name: str):
    if not isinstance(name, str) or len(name.strip()) == 0:
        raise ValueError("Name must be a non-empty string.")

def collection_validate_add(self, student):
        if student in self:
            raise ValueError("This student is already present in this group.")
        
def collection_validate_remove(self, student):
     if student not in self:
          raise ValueError("student not in group")
     
def collection_validate_remove_at(self, index):
     if not 0 <= index < len(self):
            raise IndexError("index out of range")