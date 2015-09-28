from django.conf.urls import patterns, url

from .views.views import BookPerBranchView, FieldView


urlpatterns = patterns(
    '',
    # REST

    url(r'^branch-view/(?P<branch>\w*)?$', BookPerBranchView.as_view()),
    url(r'^field/(?P<field>\w*)?$', FieldView.as_view()),
    #url(r'^guide/(?P<guide_id>[0-9]+)/step/(?P<step_id>[0-9]+)?$', GuideStepRest.as_view()),
)
