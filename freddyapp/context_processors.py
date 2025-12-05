def leecookie(request):
    theme = request.COOKIES.get('theme', 'nothing')
    return {'theme': theme}