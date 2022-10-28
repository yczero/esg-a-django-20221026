from django.contrib import messages
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
    memory = Memory.objects.get(pk=pk)  # 값 그자체 keyword??
    return render(request, 'diary/mem_detail.html', {'memory': memory, })


def mem_new(request):
    if request.method == "POST":
        form = MemoryForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            memory: Memory = form.save()

            messages.success(request, "메모리를 생성")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm()

    return render(request, "diary/mem_new.html", {
        "form": form,
    })


def mem_edit(request, pk):
    memory = Memory.objects.get(pk=pk)

    if request.method == "POST":
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            messages.success(request, "메모리를 저장")
            # form.cleaned_data
            memory = form.save()
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = MemoryForm(instance=memory)

    return render(request, "diary/mem_new.html", {
        "form": form,
    })


def mem_delete(request, pk):
    memory = Memory.objects.get(pk=pk)

    if request.method == "POST":
        memory.delete()
        messages.success(request, "메모리를 삭제")
        return redirect("/diary/")

    return render(request, 'diary/mem_confirm_delete.html', {'memory': memory, })
