#!/usr/bin/env python3
from secrets import token_hex
import os

from bot import (
    LOGGER,
    aria2_options,
    aria2c_global,
    download_dict,
    download_dict_lock,
    non_queued_dl,
    queue_dict_lock,
    config_dict,
)
from bot.helper.ext_utils.bot_utils import sync_to_async
from bot.helper.ext_utils.task_manager import is_queued, stop_duplicate_check
from bot.helper.listeners.direct_listener import DirectListener
from bot.helper.mirror_utils.status_utils.direct_status import DirectStatus
from bot.helper.mirror_utils.status_utils.queue_status import QueueStatus
from bot.helper.telegram_helper.message_utils import sendMessage, sendStatusMessage

# ✅ Import uploader
from bot.helper.mirror_utils.upload_utils.uploader import uploader


async def add_direct_download(details, path, listener, foldername):
    if not (contents := details.get("contents")):
        await sendMessage(listener.message, "There is nothing
