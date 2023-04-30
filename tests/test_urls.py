import pytest

from book.read.models import Book


class UrlsTest:
    @pytest.mark.django_db(transaction=True)
    def test_book_view_get(self, client, book):
        response = client.get('/api/books/')
        assert response.status_code != 404, (
            'Страница `/api/books/` не найдена, проверьте этот адрес в *urls.py*'
        )
    
    @pytest.mark.django_db(transaction=True)
    def test_post_list_not_auth(self, client, book):
        response = client.get('/api/books/')

        assert response.status_code == 200, (
            'Проверьте, что на `/api/books/` при запросе без токена возвращаете статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_single_not_auth(self, client, book):
        response = client.get(f'/api/books/{book.id}/')

        assert response.status_code == 200, (
            'Проверьте, что на `/api/books/{book.id}/` при запросе без токена возвращаете статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_posts_get_not_paginated(self, user_client, book):
        response = user_client.get('/api/books/')
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/books/` с токеном авторизации возвращается статус 200'
        )

        test_data = response.json()

        book = Book.objects.all()[0]
        test_book = test_data[0]
        assert 'id' in test_book, (
            'Проверьте, что добавили `id` в список полей `fields` сериализатора модели Book'
        )
        assert 'title' in test_book, (
            'Проверьте, что добавили `title` в список полей `fields` сериализатора модели Book'
        )
        assert 'author' in test_book, (
            'Проверьте, что добавили `author` в список полей `fields` сериализатора модели Book'
        )
        assert 'pub_date' in test_book, (
            'Проверьте, что добавили `pub_date` в список полей `fields` сериализатора модели Book'
        )

        assert test_book['id'] == book.id, (
            'Проверьте, что при GET запросе на `/api/books/` возвращается весь список статей'
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_create(self, user_client, book):
        data = {}
        response = user_client.post('/api/v1/posts/', data=data)
        assert response.status_code == 400, (
            'Проверьте, что при POST запросе на `/api/books/` с не правильными данными возвращается статус 400'
        )

        data = {'title': 'Книга Тест'}
        response = user_client.book('/api/books/', data=data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе на `/api/books/` с правильными данными возвращается статус 201'
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_get_current(self, user_client, book, user):
        response = user_client.get(f'/api/books/{book.id}/')

        assert response.status_code == 200, (
            'Страница `/api/books/{id}/` не найдена, проверьте этот адрес в *urls.py*'
        )

        test_data = response.json()
        assert test_data.get('title') == book.text, (
            'Проверьте, что при GET запросе `/api/books/{id}/` возвращаете данные сериализатора, '
            'не найдено или не правильное значение `title`'
        )
        assert test_data.get('author') == user.username, (
            'Проверьте, что при GET запросе `/api/books/{id}/` возвращаете данные сериализатора, '
            'не найдено или не правильное значение `author`, должно возвращать имя пользователя '
        )
    @pytest.mark.django_db(transaction=True)
    def test_post_patch_current(self, user_client, book, book_another):
        response = user_client.patch(f'/api/books/{book.id}/',
                                     data={'text': 'Поменяли текст статьи'})

        assert response.status_code == 200, (
            'Проверьте, что при PUT запросе `/api/books/{id}/` возвращаете статус 200'
        )

        test_post = Book.objects.filter(id=book.id).first()

        assert test_post, (
            'Проверьте, что при PUT запросе `/api/books/{id}/` вы не удалили статью'
        )

        assert test_post.text == 'Поменяли текст статьи', (
            'Проверьте, что при PUT запросе `/api/books/{id}/` вы изменяете статью'
        )

        response = user_client.put(f'/api/books/{book_another.id}/',
                                    data={'title': 'Поменяли название статьи'})

        assert response.status_code == 403, (
            'Проверьте, что при PUT запросе `/api/books/{id}/` для не своей статьи возвращаете статус 403'
        )

    @pytest.mark.django_db(transaction=True)
    def test_post_delete_current(self, user_client, book, book_another):
        response = user_client.delete(f'/api/books/{book.id}/')

        assert response.status_code == 204, (
            'Проверьте, что при DELETE запросе `/api/books/{id}/` возвращаете статус 204'
        )

        test_book = Book.objects.filter(id=book.id).first()

        assert not test_book, (
            'Проверьте, что при DELETE запросе `/api/books/{id}/` вы удалили статью'
        )

        response = user_client.delete(f'/api/books/{book_another.id}/')

        assert response.status_code == 403, (
            'Проверьте, что при DELETE запросе `/api/books/{id}/` для не своей статьи возвращаете статус 403'
        )
