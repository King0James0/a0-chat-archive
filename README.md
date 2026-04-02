# Chat Archive

An Agent Zero plugin that adds chat archiving capabilities to the sidebar.

![thumbnail](thumbnail.png)

## Features

### 📦 Archive Chats
Archive any chat from the sidebar to declutter your workspace. Archived chats are hidden from the sidebar but safely preserved.

### 🗄️ Archive Modal
Access all archived chats through a dedicated modal (click the archive icon next to New Chat). From the modal you can:

| Action | Description |
|--------|-------------|
| **Restore** | Move the chat back to the sidebar |
| **Delete** | Permanently remove the chat (two click confirmation) |

## Responsive Design

On small screens (≤480px), button labels in the archive modal are automatically hidden, showing only icons for a compact layout.

## Installation

1. Copy the `chat_archive` folder to `/a0/usr/plugins/`
2. Go to **Settings** → **Plugins**
3. Enable **Chat Archive**
4. Refresh the page

## Data Storage

Archive data is stored as JSON in `chat_archive/data/` with atomic writes for thread safety.

## License

MIT
