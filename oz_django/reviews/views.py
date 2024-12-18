from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import ReviewSerializer
from .models import Review

# api/v1/reviews [GET]
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        # 장고 객체 -> json
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data)

# api/v1/reviews/review_id
class ReviewDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id = review_id)
        except:
            raise NotFound

        serializer = ReviewSerializer(review)
        return Response(serializer.data)