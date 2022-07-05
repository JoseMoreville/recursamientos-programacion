from fastapi import APIRouter,UploadFile
import aiohttp

router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}}
)

@router.get("/rickymorty")
async def say_hello():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://rickandmortyapi.com/api/character/17') as response:
            return (await response.json())


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    with open("uploads/imgw.png", "wb") as obj:
        obj.write(content)
    return {"filename": file.filename}