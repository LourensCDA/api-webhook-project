"""Package router exports.

FastAPI expects an APIRouter instance to be passed to `app.include_router()`.
"""

from .leads import router as leads_router
from .webhook import router as webhook_router

# Backwards-compatible alias for code that used `routes.routes`.

router = leads_router
router.include_router(webhook_router)
