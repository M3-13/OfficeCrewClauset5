from fastapi import APIRouter

router = APIRouter(prefix="/api/items", tags=["items"])


@router.get("/", status_code=501)
async def list_items():
    raise NotImplementedError


@router.post("/", status_code=501)
async def create_item():
    raise NotImplementedError


@router.get("/{item_id}", status_code=501)
async def get_item(item_id: int):
    raise NotImplementedError


@router.put("/{item_id}", status_code=501)
async def update_item(item_id: int):
    raise NotImplementedError


@router.delete("/{item_id}", status_code=501)
async def delete_item(item_id: int):
    raise NotImplementedError
