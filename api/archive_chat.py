from helpers.api import ApiHandler, Input, Output, Request, Response
from usr.plugins.chat_archive.helpers.archive_data import archive_chat


class ArchiveChat(ApiHandler):
    """Archive a chat so it is hidden from the sidebar."""

    async def process(self, input: Input, request: Request) -> Output:
        chat_id = input.get("chat_id", "")
        if not chat_id:
            return Response("Missing chat_id", 400)

        name = input.get("name", "")
        archived_at = archive_chat(chat_id, name)

        return {
            "ok": True,
            "chat_id": chat_id,
            "archived_at": archived_at,
        }
