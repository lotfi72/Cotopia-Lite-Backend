from datetime import datetime

from pydantic import BaseModel

from db.models.room_user import VoiceStatus, VideoStatus


class RoomUserBase(BaseModel):
    user_id: int
    room_id: int


class RoomUserCreate(RoomUserBase):
    voice_status: VoiceStatus
    video_status: VideoStatus
    coordinates: str | None = None


class RoomUserUpdate(RoomUserCreate):
    voice_status: VoiceStatus | None = None
    video_status: VideoStatus | None = None
    coordinates: str | None = None
    screenshare_coordinates: str | None = None
    screenshare_size: str | None = None
    video_coordinates: str | None = None
    video_size: str | None = None


class RoomUser(RoomUserUpdate):
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
