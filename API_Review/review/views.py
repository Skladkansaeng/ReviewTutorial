from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg, Count
from .models import Review
from .serializers import ReviewSerializer
from django.contrib.auth.models import User


class ReviewView(APIView):

    def get(self, request):
        review = Review.objects.all().order_by('-id')
        average = Review.objects.aggregate(Avg('score'))
        freq = Review.objects.values('score').annotate(count=Count('score'))
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ReviewSerializer(review, many=True)
        return Response({'averages': average, 'Freq': freq, 'count_review': review.count(), 'result': serializer.data})

    def post(self, request):
        _input = request.data
        if 1 <= _input['score'] <= 5:
            user = User.objects.filter(username=_input['user'])
            if len(user) == 0:
                return Response({'Response': 'User Not Found.'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                review = Review.objects.filter(user=user[0])
                if len(review) == 0:
                    Review.objects.create(user=user[0], score=_input['score'], review=_input['review'])
                    return Response({'Response': 'Review Success.'})
                else:
                    return Response({'Response': 'user found in record.'})
        else:
            return Response({'Response': 'score out of the range.'}, status=status.HTTP_400_BAD_REQUEST)
