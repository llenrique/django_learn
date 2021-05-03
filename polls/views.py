from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .poll_helpers import poll_helper
from django.urls import reverse

from .models import Question, Choice

def index(request):
  latest_question = poll_helper.get_latest_question()
  context = {'latest_question': latest_question}
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  question = poll_helper.get_question(question_id)
  return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
  question = poll_helper.get_question(question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  question = poll_helper.get_question(question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, ChoiceDoesNotExist):
    return render(request, 'polls/detail.html', 
    {
      'question': question,
      'error_message': "You didn't select a choice"
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()

  return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))