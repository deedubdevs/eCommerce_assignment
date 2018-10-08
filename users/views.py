from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic

from stores.models import Store
from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def goto_dashboard(request):
    if request.user.is_authenticated:
        stores = get_list_or_404(
            Store.objects.order_by("name"),
            owner=request.user.id)
        context = {"stores": stores}
        return render(request, "registration/home.html", context)
    else:
        return HttpResponseRedirect(reverse("home"))


def home(request):
    stores = get_list_or_404(Store.objects.order_by("name"))
    context = {"stores": stores}
    return render(request, "registration/home.html", context)
