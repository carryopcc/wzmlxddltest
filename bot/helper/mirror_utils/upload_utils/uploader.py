from bot.helper.mirror_utils.upload_utils.pixeldrain_uploader import pixeldrain_uploader

def uploader(file_path, upload_type):
    """
    Handles file uploading based on upload_type (pixeldrain, etc.)
    """
    if upload_type == 'pixeldrain':
        return pixeldrain_uploader(file_path)
    
    raise ValueError(f"Unknown upload type: {upload_type}")
