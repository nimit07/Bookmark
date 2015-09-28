from __future__ import unicode_literals
from django.db import models
from django.utils.translation import pgettext_lazy


class BooksPerBranch(models.Model):
    branch = models.CharField(
        verbose_name=pgettext_lazy(' branch name', 'Branch'),
        max_length=5,


    )
    total_books = models.IntegerField(
        verbose_name=pgettext_lazy('total no of books', 'Total_Books')
    )

    def to_dict(self):
        dictionary = {
            'id': self.pk,
            'branch': self.branch,
            'total_books': self.total_books,
        }

        return dictionary

    def load_from_dict(self, updates):
        for field, value in updates.items():
            if hasattr(self, field):
                self.__setattr__(field, value)

    def __str__(self):
        return self.branch

    class Meta:
        app_label = 'library'


class FieldList(models.Model):
    branch = models.ForeignKey(
        BooksPerBranch,
        verbose_name=pgettext_lazy(' branch name', 'Branch'),
        related_name='branch_name'

    )
    field = models.CharField(
        verbose_name=pgettext_lazy('field of book', 'Field'),
        max_length=30
    )

    def to_dict(self):
        dictionary = {
            'branch': self.branch.to_dict(),
            'field': self.field
        }
        return dictionary

    def load_from_dict(self, updates):
        for field, value in updates.iteritems():
            if hasattr(self, field):
                self.__setattr__(field, value)

    def __str__(self):
        return self.field

    class Meta:
        app_label = 'library'


class BookManager(models.Manager):
    def get_list(self, title):
        results = self.filter(title__contains=title)
        return results.to_dict()

    def update_copies(self, title, copies, add=False):
        result = self.filter(title=title)
        prev_copies = result['copies']
        if add:
            result.update(copies=prev_copies+copies)
        else:
            result.update(copies=prev_copies-copies)
        return self.filter(title=title).to_dict()

    class Meta:
        app_label = 'library'


class BookList(models.Model):
    field = models.ForeignKey(
        FieldList,
        verbose_name=pgettext_lazy('field of book', 'Field'),
        related_name='book_field'
    )

    title = models.CharField(
        verbose_name=pgettext_lazy('Book Title', 'Title'),
        max_length=80
    )
    author = models.CharField(
        verbose_name=pgettext_lazy('Book Author', 'Author'),
        max_length=80
    )
    copies = models.IntegerField(
        verbose_name=pgettext_lazy('No of Copies', 'Copies'),

    )

    objects = BookManager()

    def to_dict(self):
        dictionary = {
            'title': self.title,
            'author': self.author,
            'copies': self.copies,
            'field': self.field.to_dict()
        }
        return dictionary

    def load_from_dict(self, updates):
        for field, value in updates.iteritems():
            if hasattr(self, field):
                self.__setattr__(field, value)

    class Meta:
        app_label = 'library'
