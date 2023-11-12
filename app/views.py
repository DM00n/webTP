from django.shortcuts import render


def index(request):
    # page_list = Question.objects.new_questions()
    # context = paginate(page_list, request, 4)
    #
    # return render(request, 'index.html',
    #               {'questions': context, 'best_members': get_best_members(), 'popular_tags': get_popular_tags()})
    return render(request, 'index.html')
