def get_name(request):
    return {'name': request.user.get_full_name() or request.user.username
            if request.user.is_authenticated else ""}
