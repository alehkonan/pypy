from typing import Dict

from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/")
def read_root() -> Dict[str, str]:
    return {"status": "sfcsff"}
