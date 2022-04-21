from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from microhr.forms import WorkerProfileForm, WorkForm
from microhr.decorators import worker_required
from logging import getLogger
from django.views.decorators.http import require_POST, require_GET


from microhr.models import Application

logger = getLogger(__name__)


@login_required
@worker_required
def resume(request):
    """履歴書表示(GET)・編集(POST)"""

    if request.method == 'POST':
        form = WorkerProfileForm(request.POST,
                                 instance=request.user.workerprofile)
        if form.is_valid():
            worker_profile = form.save()
            worker_profile.save()
            return redirect('home')
    else:
        form = WorkerProfileForm(instance=request.user.workerprofile)
    return render(request, 'resume/edit.html', {'form': form})


@login_required
@worker_required
@require_POST
def apply(request, work_id):
     
    """応募済みでないか確認"""
    check = Application.objects.filter(user_id = request.user.id, work_id = work_id)
    if check:
        return redirect('home')
    """求人へ応募する"""  
    Application.objects.create(user_id = request.user.id, work_id = work_id)
    return redirect(applied_items)
 
    
@login_required
@worker_required
def applied_items(request):   
    applications = Application.objects.select_related('work').filter(user_id=request.user.id)
    context = {"applications": applications}
    return render(request, "work/items.html", context)