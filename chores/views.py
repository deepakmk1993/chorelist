from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import ChoreList, Chore

# Create your views here.
def index(request):
    # return HttpResponse("You're at the ChoreList index. ")
    # output = ', '.join([cl.name for cl in lists])
    # return HttpResponse(output)
    chorelists = ChoreList.objects.all()
    template = loader.get_template('chores/index.html')
    context = RequestContext(request, {
        'chorelists': chorelists
    })
    return HttpResponse(template.render(context))

def detail(request, chorelist_id):
    return HttpResponse("You're looking at ChoreList #%s" % chorelist_id)

def chores(request, chorelist_id):
    return HttpResponse("You're looking at the Chores from ChoreList #%s" % chorelist_id)

def choredetail(request, chorelist_id, chore_id):
    return HttpResponse("You're looking at the Chore #%s from ChoreList #%s" % (chore_id, chorelist_id))

