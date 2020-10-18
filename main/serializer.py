from rest_framework import generics, serializers

from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'title', 'date', 'amount', 'description', 'isIncome', 'author')

# class FilterEntriesByDate(generics.ListAPIView):
#     serializer_class = EntrySerializer

#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Entry.objects.all()
#         startDate = self.request.query_params.get('startDate', None)
#         endDate = self.request.query_params.get('endDate', None)
#         if startDate is not None and endDate is not None:
#             queryset = queryset.filter(date>=startDate)
#             queryset = queryset.filter(date<=endDate)
#         return queryset
