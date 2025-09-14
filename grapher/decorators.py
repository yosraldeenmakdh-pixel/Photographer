from django.shortcuts import redirect


def NoLoggedUser(view_func):
    def inerr(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('grapher:home')
        else:
            return view_func(request, *args, **kwargs)

    return inerr