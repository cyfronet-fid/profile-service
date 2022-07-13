from typing import List, Optional

from fastapi import APIRouter

from app.schemas.popular_article_response import PopularArticlesResponse
from app.utils.request_validators import valid_limit, valid_offset

router = APIRouter()


@router.get("")
async def get_popular_articles(
    limit: Optional[int] = 3, offset: Optional[int] = 0
) -> List[PopularArticlesResponse]:
    valid_limit(limit)
    valid_offset(limit, offset)

    return [
        PopularArticlesResponse(
            label="EOSC Association looks for staff: four positions open lorem",
            description=(
                "Lorem ipsum dolor sit amet enim. Etiam ullamcorper. Suspendisse a"
                " pellentesque dui, non felis. Maecenas malesuada elit lectus felis,"
                " malesuada ultricies."
            ),
            publish_date="2001-10-02T02:48:59Z",
        ),
        PopularArticlesResponse(
            label="EOSC Association looks for staff: four positions open lorem",
            description=(
                "Lorem ipsum dolor sit amet enim. Etiam ullamcorper. Suspendisse a"
                " pellentesque dui, non felis. Maecenas malesuada elit lectus felis,"
                " malesuada ultricies."
            ),
            publish_date="2001-10-02T02:48:59Z",
        ),
        PopularArticlesResponse(
            label="EOSC Association looks for staff: four positions open lorem",
            description=(
                "Lorem ipsum dolor sit amet enim. Etiam ullamcorper. Suspendisse a"
                " pellentesque dui, non felis. Maecenas malesuada elit lectus felis,"
                " malesuada ultricies."
            ),
            publish_date="2001-10-02T02:48:59Z",
        ),
    ][offset:limit]
