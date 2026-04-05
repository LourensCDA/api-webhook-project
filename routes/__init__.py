"""Package router exports.

FastAPI expects an APIRouter instance to be passed to `app.include_router()`.
"""

from .tasks import router as router

# Backwards-compatible alias for code that used `routes.routes`.
routes = router
