# lab06/container.py

from typing import TypeVar, Generic, Callable, Optional, List
from abc import abstractmethod

class Displayable:
    @abstractmethod
    def __str__(self) -> str:
        # return the string rep of an obj
        ...

class Scorable:
    @abstractmethod
    def score(self) -> float:
        # returns a numerical "score" of an obj
        ...

T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> bool:
        if item in self._items:
            self._items.remove(item)
            return True
        return False
    
    def get_all(self) -> List[T]:
        return self._items.copy()
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]
    
    def get_first_display(self) -> Optional[str]:
        if self._items:
            return self._items[0].display()  # type: ignore
        return None
    
    def get_scores(self) -> List[float]:
        return [item.score() for item in self._items]  # type: ignore
    
    def __str__(self) -> str:
        if not self._items:
            return "collection empty"
        
        result = f"TypedCollection (total: {len(self._items)} elements)\n"
        result += "-" * 40 + "\n"
        for i, item in enumerate(self._items, 1):
            result += f"{i}. {item}\n"
        result += "-" * 40
        return result

# collections that work with displayable
DisplayableCollection = TypedCollection[D]

# collections that work with scoreable
ScorableCollection = TypedCollection[S]