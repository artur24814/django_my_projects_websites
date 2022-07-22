from .models import Words, RandomWordForHomeView
import random



def random_word_for_home_view():
    """
    view for crontab.
    if crontab make word Day firs time or delete and creating new word day for home view if he did it jet
    """
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
