from django.http import HttpResponse
from django.views import View
from demo.models import Book


class Second(View):

    def get(self, request):
        books = Book.objects.all()
        output = ''
        for book in books:
            output += f'We have {book.title} with ID {book.id} in our Database <br>'
        return HttpResponse(output)



