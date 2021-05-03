
from django.shortcuts import get_object_or_404
from ..models import Question

def get_latest_question():
  return Question.objects.order_by('-pud_date')[:5]

def get_question(question_id):
  return get_object_or_404(Question, pk=question_id)
