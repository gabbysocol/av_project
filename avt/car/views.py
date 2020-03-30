from datetime import date
from django.shortcuts import render
# from .forms import UserForm


# def landing(request):
#     """
#     Function for getting html-template.
#
#     """
#     name = "USER"
#     current_day = str(date.today())
#     form = UserForm(request.POST or None)
#
#     if request.method == 'POST' and form.is_valid():
#         print(form.cleaned_data)
#
#         new_data = form.save()

    # context=data for render()
    # return render(request, 'login/login.html', locals())
