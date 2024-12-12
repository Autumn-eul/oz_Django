from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only = True)
    review_set = ReviewSerializer(many = True, read_only = True)
    class Meta:
        model = Feed # 직렬화 하고싶다
        fields = "__all__" # Feed 라는 모델에 있는 전체 fields 를 직렬화 하길 원한다
        depth = 1

        """
        depth = 0 은 username 만 가져온다
        depth = 1 은 user 데이터에 있는 모든 정보를 확인할 수 있는데 그것을 제한하기 위해
        UserSerializers 를 생성하여 정보를 제한함
        """