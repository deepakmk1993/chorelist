from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ChoreList, Chore
# from django.template import RequestContext, loader

def index(request):
    # return HttpResponse("You're at the ChoreList index. ")
    # output = ', '.join([cl.name for cl in lists])
    # return HttpResponse(output)
    # template = loader.get_template('chores/index.html')
    # context = RequestContext(request, {
    #     'chorelists': chorelists
    # })
    # return HttpResponse(template.render(context))
    lists = ChoreList.objects.all()
    return render(request, 'chores/index.html', { 'chorelists': lists })

def newlist(request):
    if request.POST:
        list = ChoreList(name=request.POST['name'], due_date=request.POST['duedate'])
        list.save()
        return HttpResponseRedirect('/chores')
    else:
        return render(request, 'chores/newlist.html', {})

def detail(request, chorelist_id):
    # return HttpResponse("You're looking at ChoreList #%s" % chorelist_id)
    list = get_object_or_404(ChoreList, pk=chorelist_id)
    return render(request, 'chores/detail.html', { 'chorelist': list })

def choredetail(request, chorelist_id, chore_id):
    # return HttpResponse("You're looking at the Chore #%s from ChoreList #%s" % (chore_id, chorelist_id))
    list = get_object_or_404(ChoreList, pk=chorelist_id)
    chore = get_object_or_404(Chore, pk=chore_id)
    return render(request, 'chores/choredetail.html', { 'chorelist': list, 'chore': chore })

def updatechore(request, chorelist_id, chore_id):
    chore = get_object_or_404(Chore, pk=chore_id)
    if 'complete' in request.POST:
        chore.complete = True
    else:
        chore.complete = False
    chore.save()
    return HttpResponseRedirect('/chores/' + chorelist_id + '/chores/' + chore_id)
