from datacenter.models import Mark,Schoolkid,Chastisement,Commendation,Subject,Lesson,Teacher
import random




def fix_marks(kidname):
    '''  исправляем оценки'''
    try:
        schoolkid=Schoolkid.objects.get(full_name__contains=kidname)
        schoolkid_and_points=Mark.objects.filter(schoolkid=schoolkid,points__lte=3)

        for schoolkid_and_point in schoolkid_and_points:
                schoolkid_and_point.points=5
                schoolkid_and_point.save()
    except Schoolkid.DoesNotExist:
        print('Такого ученика нет в этой школе ')
        
    except Schoolkid.MultipleObjectsReturned:
        print('Скрипт нашел несколько учеников')



kidname='Соболев Арсений'
fix_marks(kidname)




def remove_chastisements(kidname):
    '''удаляем замечания '''
    try:
        schoolkid=Schoolkid.objects.get(full_name__contains=kidname)
        chastisements=Chastisement.objects.filter(schoolkid=schoolkid)
        for chastisement in chastisements:
                chastisement.delete()

    except Schoolkid.DoesNotExist:
        print('Такого ученика нет в этой школе ')
        
    except Schoolkid.MultipleObjectsReturned:
        print('Скрипт нашел несколько учеников')

kidname='Соболев Арсений'
remove_chastisements(kidname)



def add_commendation(kidname,subject,text):
    '''Добавляем похвалу '''
    try:
        schoolkid=Schoolkid.objects.get(full_name__contains=kidname)
        lessons=Lesson.objects.filter(group_letter='А',subject=subject[0]).order_by('-date')
        teacher=lessons[0].teacher
        date=lessons[0].date
        commendation=Commendation.objects.create(text=text,schoolkid=schoolkid,subject=subject[0],teacher=teacher,created=date)
    except Schoolkid.DoesNotExist:
        print('Такого ученика нет в этой школе ')
        
    except Schoolkid.MultipleObjectsReturned:
        print('Скрипт нашел несколько учеников')
        
      

kidname='Соболев Арсений'
subject=Subject.objects.filter(title='Технология',year_of_study=6)
commendations=['Молодец!','Отлично!','Хорошо!','Гораздо лучше, чем я ожидал!','Ты меня приятно удивил!','Великолепно!','Прекрасно!','Ты меня очень обрадовал!','Именно этого я давно ждал от тебя!','Сказано здорово – просто и ясно!','Ты, как всегда, точен!','Очень хороший ответ!','Талантливо!','Ты сегодня прыгнул выше головы!','Я поражен!','Уже существенно лучше!','Потрясающе!','Замечательно!','Прекрасное начало!','Так держать!','Ты на верном пути!','Здорово!','Это как раз то, что нужно!','Я тобой горжусь!','С каждым разом у тебя получается всё лучше!','Мы с тобой не зря поработали!','Я вижу, как ты стараешься!','Ты растешь над собой!','Ты многое сделал, я это вижу!','Теперь у тебя точно все получится!']

add_commendation(kidname,subject,random.choice(commendations))

