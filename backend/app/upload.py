from fastapi import UploadFile


async def save_upload(file: UploadFile, upload_dir: str) -> str:
    raise NotImplementedError


async def validate_image(file: UploadFile) -> None:
    raise NotImplementedError
