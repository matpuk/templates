from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/workspaces')


@router.get('/')
async def get_workspaces():
    return []


@router.get('/{ws_id:int}')
async def get_workspace_by_id(ws_id: int):
    return {'workspaceId': ws_id, 'alias': ''}


@router.get('/{alias:str}')
async def get_workspace_by_alias(alias: str):
    return {'workspaceId': 10, 'alias': alias}
