from .models import Words, RandomWordForHomeView
import random



def random_word_for_home_view():
    # list = Words.objects.all()
    # random_word = random.choice(list)
    # RandomWordForHomeView.objects.create(word=random_word)
    delete_list = RandomWordForHomeView.objects.all()
    # if we do not have any word created jet
    if len(delete_list) < 1:
        list = Words.objects.all()
        random_word = random.choice(list)
        word_for_home_view = RandomWordForHomeView.objects.create(word=random_word)
        return 'ok'
    #if crontab already created somethings
    else:
        delete_list.delete()
        list = Words.objects.all()
        random_word = random.choice(list)
        word_for_home_view = RandomWordForHomeView.objects.create(word=random_word)
