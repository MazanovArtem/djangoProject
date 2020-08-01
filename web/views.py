from django.shortcuts import render, redirect
from djangoProject import settings
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html', context={
        'email': '123@123.ru',
        'phone': '+7-999-123-12-12',
        'server_time': datetime.now()
    })


publications_data = [{
        'id': 0,
        'title': 'Публикация 0',
        'text': "<i>Lorem Ipsum</i> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        'date': datetime.now()
    },
    {
        'id': 1,
        'title': 'Публикация 1',
        'text': "<i>Lorem Ipsum</i> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        'date': datetime.now()
    },
    {
        'id': 2,
        'title': 'Публикация 2',
        'text': "<i>Lorem Ipsum</i> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        'date': datetime.now()
    }
]


def publications(request):
    return render(request, 'publications.html', context={
        'publications': reversed(publications_data)
    })


def publication(request, number):
    if number >= len(publications_data):
        return redirect('/publications')
    return render(request, 'publication.html', context=publications_data[number])


def publish(request):
    if request.method == 'POST':
        data = request.POST
        password = data.get('password', '')
        title = data.get('title', '')
        text = data.get('text', '')
        if not password or not title:
            return render(request, 'publish.html', {'error': 'Есть пустое поле'})
        if password != settings.PUBLISH_PASSWORD:
            return render(request, 'publish.html', {'error': 'Неверный пароль'})
        publications_data.append({
            'id': len(publications_data),
            'title': title,
            'date': datetime.now(),
            'text': text
        })
        return redirect('/publications/' + str(publications_data[-1]['id']))
    return render(request, 'publish.html')
