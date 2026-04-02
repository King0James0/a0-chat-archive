from helpers.api import ApiHandler, Input, Output, Request
from usr.plugins.chat_archive.helpers.archive_data import get_archived


class GetArchived(ApiHandler):
    """Return all archived chats with metadata."""

    async def process(self, input: Input, request: Request) -> Output:
        archived = get_archived()
        return {
            "ok": True,
            "archived": archived,
        }
