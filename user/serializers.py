from rest_framework import serializers
from .models import Book,Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_id = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'

    def create(self,validated_data):
        author = validated_data.pop('author_id',None)
        print(author)
        author = Author.objects.create(**author)
        book = Book.objects.create(author_id=author,**validated_data)
        return book