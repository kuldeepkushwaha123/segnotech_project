from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
# Create your views here.





def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, "polls/detail.html", {"question": question})



def results(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, "polls/results.html", {"question": question})


def vote(request, slug):
    question = get_object_or_404(Question, slug=slug)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.slug,)))