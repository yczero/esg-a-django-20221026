from django.shortcuts import render, redirect
from diary.models import Memory
from diary.forms import MemoryForm


# Create your views here.
def mem_index(request):
    # 전체 포스팅을 가지고 올 준비 아직 안 가지고옴
    mem_qs = Memory.objects.all().order_by('-id')
    return render(request, 'diary/mem_list.html', {
        'mem_list': mem_qs, })


def mem_detail(request, pk):
    post = Memory.objects.get(pk=pk)  # 값 그자체 keyword??
    return render(request, 'diary/mem_detail.html', {'post': post, })


def mem_new(request):
    # print("request.method = " , request.method)
    # print("request.post = " , request.POST)
    if request.method == "GET": # POST
        form = MemoryForm()
    else:
        form = MemoryForm(request.POST)
        if form.is_valid():  # 유효성 검사?? 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save()  # ModelForm  에서 지원
            # return redirect('/blog/')
            # return redirect(f"/blog/{ post.pk }/")
            # return redirect(post.get_absolute_url())
            return redirect(post)
          # return redirect ( f"/diary/{memomry.pk}/")
          # return redirect ( memomry.get_absolute_url())

    return render(request, "diary/mem_new.html", {'form': form, })
