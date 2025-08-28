from typing import Dict, List

from app.schemas.items import Item, ItemCreate


class ItemsService:
    def __init__(self) -> None:
        self._store: Dict[int, Item] = {}
        self._next_id: int = 1

    def list_items(self) -> List[Item]:
        return list(self._store.values())

    def get_item(self, item_id: int) -> Item | None:
        return self._store.get(item_id)

    def create_item(self, payload: ItemCreate) -> Item:
        item = Item(id=self._next_id, **payload.dict())
        self._store[self._next_id] = item
        self._next_id += 1
        return item

    def update_item(self, item_id: int, payload: ItemCreate) -> Item | None:
        if item_id not in self._store:
            return None
        updated = Item(id=item_id, **payload.dict())
        self._store[item_id] = updated
        return updated

    def delete_item(self, item_id: int) -> bool:
        if item_id not in self._store:
            return False
        del self._store[item_id]
        return True
