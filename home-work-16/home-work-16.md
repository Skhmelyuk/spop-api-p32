# 📝 Домашнє завдання 16: Django REST Framework - Generic Views

## 🎯 Мета завдання

Закріпити знання з використання Generic Views у Django REST Framework, отримані на уроці:
- Перехід з function-based views на class-based views (CBV)
- Використання базових Generic Views (`ListAPIView`, `RetrieveAPIView`, `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`)
- Налаштування `queryset`, `serializer_class`
- Використання `lookup_url_kwarg` для кастомізації URL-параметрів
- Фільтрація QuerySet у класових представленнях

---

## 📚 Завдання: Рефакторинг та розширення API для бібліотеки

Ви продовжуєте розробляти REST API для системи управління бібліотекою з попереднього домашнього завдання (Домашнє завдання 15). Ваше завдання — переписати всі існуючі views на **Generic Views** та розширити їх функціонал, додавши можливості створення, оновлення та видалення об'єктів.

---

## 🛠️ Частина 1: Перехід на Generic Views (40 балів)

Відкрийте файл `library/views.py` та замініть існуючі функції (з декоратором `@api_view`) на класи, що успадковуються від `rest_framework.generics`.

### 1.1 Author Views (15 балів)
- Замініть `author_list` на клас **`AuthorListCreateAPIView`**, що успадковується від `generics.ListCreateAPIView`.
  - Це дозволить не тільки отримувати список авторів (GET), але й створювати нових (POST).
- Замініть `author_detail` на клас **`AuthorDetailAPIView`**, що успадковується від `generics.RetrieveUpdateDestroyAPIView`.
  - Це дозволить отримувати (GET), оновлювати (PUT/PATCH) та видаляти (DELETE) автора.

### 1.2 Book Views (15 балів)
- Замініть `book_list` на клас **`BookListCreateAPIView`** (`generics.ListCreateAPIView`).
- Замініть `book_detail` на клас **`BookDetailAPIView`** (`generics.RetrieveUpdateDestroyAPIView`).

### 1.3 Borrowing View (10 балів)
- Замініть `borrowing_list` на клас **`BorrowingListCreateAPIView`** (`generics.ListCreateAPIView`).
  - Тепер ви зможете не лише переглядати історію позик, але й реєструвати нову позику (POST).

---

## 🔍 Частина 2: Фільтрація та кастомізація (20 балів)

### 2.1 Available Books (10 балів)
- Замініть функцію `available_books` на клас **`AvailableBookListAPIView`** (успадковується від `generics.ListAPIView`).
- Перевизначте `queryset` так, щоб він повертав лише ті книги, які є в наявності (`available_copies__gt=0` або аналогічна умова, залежно від вашої моделі з минулого завдання).

### 2.2 Зміна lookup_url_kwarg (10 балів)
- Для класу `AuthorDetailAPIView` налаштуйте атрибут `lookup_url_kwarg = 'author_id'`. Це означає, що DRF буде шукати параметр `author_id` у вашому URL замість стандартного `pk`.

---

## 🌐 Частина 3: Оновлення URLs (20 балів)

Оновіть файл `library/urls.py`, щоб використовувати ваші нові class-based views. Пам'ятайте, що класи підключаються за допомогою методу `.as_view()`.

Зверніть особливу увагу на URL для деталей автора, де потрібно використати `<int:author_id>` замість `<int:pk>`.

Приклад частини вашого файлу `urls.py`:
```python
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    # Authors
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author_list_create'),
    path('authors/<int:author_id>/', views.AuthorDetailAPIView.as_view(), name='author_detail'), # Зверніть увагу на author_id
    
    # ... додайте інші шляхи для Book та Borrowing ...
]
```

---

## 🧪 Частина 4: Тестування через Browsable API (20 балів)

Запустіть ваш локальний сервер:
```bash
python manage.py runserver
```

Завдяки переходу на `ListCreateAPIView` та `RetrieveUpdateDestroyAPIView`, Django REST Framework автоматично надасть вам зручні HTML-форми в браузері.

1. Перейдіть на http://127.0.0.1:8000/api/authors/
   - Створіть нового автора, використовуючи форму внизу сторінки.
2. Перейдіть на http://127.0.0.1:8000/api/books/
   - Створіть нову книгу.
3. Перейдіть на сторінку конкретного автора (наприклад, http://127.0.0.1:8000/api/authors/1/).
   - Спробуйте оновити його ім'я через форму PUT та натисніть "PUT".
   - Спробуйте видалити автора, натиснувши кнопку "DELETE".
4. Перевірте ендпоінт http://127.0.0.1:8000/api/books/available/, щоб впевнитися, що фільтрація працює правильно і ви бачите лише доступні книги.

---

## 💡 Підказки

1. Не забудьте додати імпорт: `from rest_framework import generics`.
2. В кожному класовому представленні (view) вам обов'язково потрібно вказати `queryset` та `serializer_class`.
3. Завдяки Generic Views обсяг коду у `views.py` значно зменшиться, але функціональність вашого API зросте (з'являться методи POST, PUT, DELETE).
4. Якщо виникає помилка "Expected view ... to be called with a URL keyword argument named 'pk'", перевірте, чи правильно ви налаштували `lookup_url_kwarg` у view та параметр у `urls.py`.

---

## 📚 Корисні посилання

- [DRF Generic Views Documentation](https://www.django-rest-framework.org/api-guide/generic-views/)
- [DRF Filtering](https://www.django-rest-framework.org/api-guide/filtering/)

---

## ⏰ Термін здачі

**Дедлайн:** Вказує викладач

**Удачі! 🚀**
