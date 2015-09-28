from django.core.paginator import Paginator
from ..models import BooksPerBranch, BookList, FieldList


class BooksPerBranchApi(object):
    @classmethod
    def get_list(cls, order_by=['branch'], page='1', items_per_page=10):

        books_list = BooksPerBranch.objects.order_by(*order_by)
        if page == -1:
            return books_list, None

        paginator = Paginator(books_list, items_per_page)
        books = paginator.page(page)
        return books, paginator

    @classmethod
    def get(cls, branch=None):

        try:
            book_list = BooksPerBranch.objects.get(branch=branch)
            return book_list
        except BooksPerBranch.DoesNotExist as e:
            raise e

    @classmethod
    def create(cls, data):

        # check if branch is present:
        if 'branch' not in data or data['branch'] is None:
            print 'Invalid Branch'

        book_list = BooksPerBranch(**data)
        book_list.save()
        return book_list

    @classmethod
    def delete(cls, branch=None):
        try:
            branch = BooksPerBranch.objects.get(branch=branch)
            branch.delete()
            return branch
        except BooksPerBranch.DoesNotExist as e:
            raise e

    @classmethod
    def update(cls, branch, data):

        try:
            branch_books = BooksPerBranch.objects.get(branch=branch)

            branch_books.load_from_dict(**data)
            branch_books.save()
            return branch_books

        except BooksPerBranch.DoesNotExist as e:
            raise e


class FieldListApi(object):

    @classmethod
    def get_list(cls, order_by=['branch'], page='1', items_per_page=10):

        fields_list = FieldList.objects.order_by(*order_by)
        if page == -1:
            return fields_list, None

        paginator = Paginator(fields_list, items_per_page)
        books = paginator.page(page)
        return books, paginator

    @classmethod
    def get(cls, field=None):
        try:
            field_list = FieldList.objects.get(field=field)
            return field_list
        except FieldList.DoesNotExist:
            print 'Field not found'

    @classmethod
    def create(cls, data):

        # check if branch is present:
        if 'field' not in data or data['field'] is None:
            print 'Invalid Name'

        field_list = FieldList(**data)
        field_list.save()
        return field_list

    @classmethod
    def delete(cls, field=None):
        try:
            field = FieldList.objects.get(field=field)
            field.delete()
            return field
        except FieldList.DoesNotExist:
            print 'Field not found'

    @classmethod
    def update(cls, field, data):

        try:
            field_list = FieldList.objects.get(field=field)

            field_list.load_from_dict(**data)
            field_list.save()
            return field_list

        except FieldList.DoesNotExist:
            print 'Field not found'


class BooksListApi(object):

    @classmethod
    def get_list(cls, order_by=['title'], page='1', items_per_page=10):

        books_list = BookList.objects.order_by(*order_by)
        if page == -1:
            return books_list, None

        paginator = Paginator(books_list, items_per_page)
        books = paginator.page(page)
        return books, paginator

    @classmethod
    def get(cls, title=None):
        try:
            books_list = BookList.objects.filter(title__contains=title)
            return books_list
        except BookList.DoesNotExist:
            print 'books not found'

    @classmethod
    def create(cls, data):

        # check if title is present:
        if 'title' not in data or data['title'] is None:
            print 'Invalid Name'

        books_list = BookList(**data)
        books_list.save()
        return books_list

    @classmethod
    def delete(cls, title=None):
        try:
            book = BookList.objects.get(title=title)
            book.delete()
            return book
        except BookList.DoesNotExist:
            print 'Book not found'

    @classmethod
    def update(cls, title, data):

        try:
            _list = BookList.objects.get(title=title)

            _list.load_from_dict(**data)
            _list.save()
            return _list

        except BookList.DoesNotExist:
            print 'Book not found'
