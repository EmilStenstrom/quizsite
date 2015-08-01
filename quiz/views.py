# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from quiz.models import Quiz

def startpage(request):
    context = {
        "quizzes": Quiz.objects.all(),
    }
    return render(request, "quiz/startpage.html", context)

def quiz(request, slug):
    try:
        quiz = Quiz.objects.get(slug=slug)
    except Quiz.DoesNotExist:
        raise Http404

    context = {
        "quiz": quiz,
    }
    return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
    number = int(number)
    try:
        quiz = Quiz.objects.get(slug=slug)
    except Quiz.DoesNotExist:
        raise Http404

    questions = quiz.questions.all()

    if request.POST:
        answer = int(request.POST["answer"])
        saved_answers = {}

        if quiz.slug in request.session:
            saved_answers = request.session[quiz.slug]

        saved_answers[str(number)] = answer
        request.session[quiz.slug] = saved_answers

        if questions.count() == number:
            return redirect("completed_page", quiz.slug)
        else:
            return redirect("question_page", quiz.slug, number + 1)

    if number > questions.count():
        raise Http404

    question = questions[number - 1]

    context = {
        "question_number": number,
        "question": question.question,
        "answer1": question.answer1,
        "answer2": question.answer2,
        "answer3": question.answer3,
        "quiz": quiz,
    }
    return render(request, "quiz/question.html", context)

def completed(request, slug):
    try:
        quiz = Quiz.objects.get(slug=slug)
    except Quiz.DoesNotExist:
        raise Http404

    questions = quiz.questions.all()
    saved_answers = request.session[slug]

    correct = 0
    for counter, question in enumerate(questions):
        if question.correct == saved_answers[str(counter + 1)]:
            correct += 1

    context = {
        "correct": correct,
        "total": questions.count(),
    }
    return render(request, "quiz/completed.html", context)
