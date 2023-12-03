from app.use_cases.ports.picture_service import IPictureService


class PictureService(IPictureService):
    def get_picture_url(self) -> str:
        return (
            "https://sticker.fpg.com.tw/sticker/festival-photo/festival-photo-042.jpg"
        )
