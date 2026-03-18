class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj
