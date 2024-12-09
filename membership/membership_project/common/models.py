from django.db import models

class CommonModel(models.Model):
    # 다른 모델들이 상속 받을 때 생성되는 시간
    created_at = models.DateTimeField(auto_now_add = True)
    # 업데이트 시간
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True