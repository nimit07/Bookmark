from django.views.generic import View
from ..api.api import BooksPerBranchApi, FieldListApi
import json

from django.http import JsonResponse
from django.http import HttpResponse


class BookPerBranchView(View):
    http_method_names = ['get', 'put', 'post', 'delete']

    def get(self, request, **kwargs):
        if kwargs.get('branch', None) is not None:
            branch = kwargs.get('branch')
            try:
                branch_data = BooksPerBranchApi.get(branch)
                response = branch_data.to_dict()
                return JsonResponse(response, safe=False)
            except Exception as e:
                return HttpResponse(e)

        else:
            order_by = request.GET.get('orderBy', 'branch').split(',')
            items_per_page = 10
            try:
                page = int(request.GET.get('page', 1))
            except ValueError:
                page = 1

            try:
                _list, paginator = BooksPerBranchApi.get_list(order_by=order_by,
                                                              items_per_page=items_per_page,
                                                              page=page)
                if paginator is None:
                    _list = [branch_list.to_dict() for branch_list in _list]
                    response = {'branch_data': _list}
                else:
                    _list = [branch_list.to_dict() for branch_list in _list.object_list]
                    response = _list

                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e

    def post(self, request):
        try:
            data = json.loads(request.body)
        except Exception as e:
            raise e

        try:
            branch_data = BooksPerBranchApi.create(data)
            response = branch_data.to_dict()
            return JsonResponse(response, safe=False)
        except Exception as e:
            raise e

    def put(self, request, **kwargs):

        if kwargs.get('branch', None) is not None:
            branch = kwargs.get('branch')

            try:
                data = json.loads(request.body)
            except Exception as e:
                raise e

            try:
                branch_data = BooksPerBranchApi.update(branch, data)
                response = branch_data.to_dict()
                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e
        else:
            return HttpResponse('null')

    def delete(self, request, **kwargs):

        if kwargs.get('branch', None) is not None:
            branch = kwargs.get('branch')
            print branch

            try:
                branch_data = BooksPerBranchApi.delete(branch)
                response = branch_data.to_dict()
                return JsonResponse(response, safe=True)
            except Exception as e:
                return e
        else:
            pass


class FieldView(View):
    http_method_names = ['get', 'put', 'post', 'delete']

    def get(self, request, **kwargs):
        if kwargs.get('branch', None) is not None:
            field = kwargs.get('field')
            try:
                field_data = FieldListApi.get(field)
                response = field_data.to_dict()
                return JsonResponse(response, safe=True)
            except Exception as e:
                raise e

        else:
            order_by = request.GET.get('orderBy', 'branch').split(',')
            items_per_page = 10
            try:
                page = int(request.GET.get('page', 1))
            except ValueError:
                page = 1

            try:
                _list, paginator = FieldListApi.get_list(order_by=order_by, items_per_page=items_per_page, page=page)
                if paginator is None:
                    _list = [branch_list.to_dict() for branch_list in _list]
                    response = {'field_data': _list}
                else:
                    _list = [field_list.to_dict() for field_list in _list.object_list]
                    response = _list

                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e

    def post(self, request, **kwargs):
        try:
            data = json.loads(request.body)
        except Exception as e:
            raise e

        try:
            field_data = FieldListApi.create(data)
            response = field_data.to_dict()
            return JsonResponse(response, safe=False)
        except Exception as e:
            raise e

    def put(self, request, **kwargs):

        if kwargs.get('field', None) is not None:
            branch = kwargs.get('field')

            try:
                data = json.loads(request.body)
            except Exception as e:
                raise e

            try:
                field_data = FieldListApi.update(branch, data)
                response = field_data.to_dict()
                return JsonResponse(response, safe=False)
            except Exception as e:
                raise e
        else:
            pass

    def delete(self, request,  **kwargs):

        if kwargs.get('field', None) is not None:
            field = kwargs.get('field')

            try:
                field_data = FieldListApi.delete(field)
                response = field_data.to_dict()
                return JsonResponse(response, safe=True)
            except Exception as e:
                return e
        else:
            pass
