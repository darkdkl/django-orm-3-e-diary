from datacenter.models import Mark,Schoolkid,Chastisement,Commendation,Subject,Lesson,Teacher
import random




def fix_marks(kidname):
    """  Исправляем оценки. """
    try:
        schoolkid=Schoolkid.objects.get(full_name__contains=kidname)
        schoolkid_points=Mark.objects.filter(schoolkid=schoolkid,points__lte=3)

        for schoolkid_point in schoolkid_points:
                schoolkid_point.points=5
                schoolkid_point.save()
    except Schoolkid.DoesNotExist:
        print('Такого ученика нет в этой школе ')
        
    except Schoolkid.MultipleObjectsReturned:
        print('Скрипт нашел несколько учеников')





def remove_chastisements(kidname):
    """ Удаляем замечания. """
    try:
        schoolkid=Schoolkid.objects.get(full_name__contains=kidname)
        chastisements=Chastisement.objects.filter(schoolkid=schoolkid)
        for chastisement in chastisements:
                chastisement.delete()

    except Schoolkid.DoesNotExist:
        print('Такого ученика нет в этой школе ')
        
    except Schoolkid.MultipleObjectsReturned:
        print('Скрипт нашел несколько учеников')


def add_commendation(kidname):
    """ Добавляем похвалу. """
    try:
        subject=Subject.objects.get(title='Технология',year_of_study=6)
        commendations=['Молодец!','Отлично!','Хорошо!','Гораздо лучше, чем я ожидал!','Ты меня приятно удивил!','Великолепно!','Прекрасно!','Ты меня очень обрадовал!','Именно этого я давно ждал от тебя!','Сказано здорово – просто и ясно!','Ты, как всегда, точен!','Очень хороший ответ!','Талантливо!','Ты сегодня прыгнул выше головы!','Я поражен!','Уже существенно лучше!','Потрясающе!','Замечательно!','Прекрасное начало!','Так держать!','Ты на верном пути!','Здорово!','Это как раз то, что нужно!','Я тобой горжусь!','С каждым разом у тебя получается всё лучше!','Мы с тобой не зря поработали!','Я вижу, как ты стараешься!','Ты растешь над собой!','Ты многое сделал, я это вижу!','Теперь у тебя точно все получится!']
        schoolkid=Schoolkid.objects.get(full_name__contains=kidname)
        lesson=Lesson.objects.get(group_letter='А',subject=subject).order_by('-date')
        teacher=lesson.teacher
        date=lesson.date
        commendation=Commendation.objects.create(text=random.choice(commendations),schoolkid=schoolkid,subject=subject,teacher=teacher,created=date)
    except Schoolkid.DoesNotExist:
        print('Такого ученика нет в этой школе ')
        
    except Schoolkid.MultipleObjectsReturned:
        print('Скрипт нашел несколько учеников')
        
      
