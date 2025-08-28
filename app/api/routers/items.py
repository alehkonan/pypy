from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.schemas.items import Item, ItemCreate
from app.services.items_service import ItemsService


def get_items_service() -> ItemsService:
    # In a real app, wire to a DB-backed service here
    return ItemsService()


router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=List[Item])
def list_items(service: ItemsService = Depends(get_items_service)) -> List[Item]:
    return service.list_items()


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, service: ItemsService = Depends(get_items_service)) -> Item:
    item = service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("", response_model=Item, status_code=201)
def create_item(
    payload: ItemCreate, service: ItemsService = Depends(get_items_service)
) -> Item:
    return service.create_item(payload)


@router.put("/{item_id}", response_model=Item)
def update_item(
    item_id: int,
    payload: ItemCreate,
    service: ItemsService = Depends(get_items_service),
) -> Item:
    updated = service.update_item(item_id, payload)
    if updated is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated


@router.delete("/{item_id}", status_code=204)
def delete_item(
    item_id: int, service: ItemsService = Depends(get_items_service)
) -> None:
    ok = service.delete_item(item_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
