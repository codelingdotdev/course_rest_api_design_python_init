from ninja import Router

router = Router()


@router.get("/bark/")
def bark(request):
    """
    Bark endpoint that returns a simple message.
    """
    return {"message": "bark!"}
