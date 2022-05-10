


from book.models import User_book
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_book
        fields = ['id','book_name','book_author',]

