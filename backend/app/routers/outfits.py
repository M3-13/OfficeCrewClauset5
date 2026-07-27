from fastapi import APIRouter

router = APIRouter(prefix="/api/outfits", tags=["outfits"])


@router.get("/", status_code=501)
async def list_outfits():
    raise NotImplementedError


@router.post("/", status_code=501)
async def create_outfit():
    raise NotImplementedError


@router.get("/{outfit_id}", status_code=501)
async def get_outfit(outfit_id: int):
    raise NotImplementedError


@router.put("/{outfit_id}", status_code=501)
async def update_outfit(outfit_id: int):
    raise NotImplementedError


@router.delete("/{outfit_id}", status_code=501)
async def delete_outfit(outfit_id: int):
    raise NotImplementedError
