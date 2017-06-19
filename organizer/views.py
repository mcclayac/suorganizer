from django.http.response import HttpResponse
from django.template import Context, loader
from django.template.loader import render_to_string



from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template(
        'organizer/tag_list.html')
    context = Context({'tag_list': tag_list})

    #rendered = render_to_string('organizer/tag_list.html', {'foo': 'bar'})
    rendered = render_to_string('organizer/tag_list.html', {'tag_list': tag_list})
    # output = template.render(tag_list)
    return HttpResponse(rendered)