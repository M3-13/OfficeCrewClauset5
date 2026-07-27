from fastapi import APIRouter

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", status_code=501)
async def register():
    raise NotImplementedError


@router.post("/login", status_code=501)
async def login():
    raise NotImplementedError


@router.post("/logout", status_code=501)
async def logout():
    raise NotImplementedError


@router.post("/refresh", status_code=501)
async def refresh():
    raise NotImplementedError
