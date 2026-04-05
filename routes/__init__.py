"""Package router exports.

FastAPI expects an APIRouter instance to be passed to `app.include_router()`.
"""

from .tasks import router as tasks_router
from .leads import router as leads_router

# Backwards-compatible alias for code that used `routes.routes`.

router = tasks_router
router.include_router(leads_router)
