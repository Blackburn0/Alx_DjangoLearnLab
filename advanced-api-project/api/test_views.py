from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", publication_year=1998, author=self.author)
        self.book_list_url = '/api/books/'
        self.book_detail_url = f'/api/books/{self.book1.id}/'

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1999,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url + 'create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        data = {
            "title": "Harry Potter and the Philosopher's Stone - Updated",
            "publication_year": 1997,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url + 'update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, data['title'])

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url + 'delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        response = self.client.get(self.book_list_url + '?publication_year=1997')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_search_books(self):
        response = self.client.get(self.book_list_url + '?search=Chamber')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title)

    def test_order_books(self):
        response = self.client.get(self.book_list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.book1.title)
        self.assertEqual(response.data[1]['title'], self.book2.title)