import os
import django
from dotenv import load_dotenv


load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь

    passcards = Passcard.objects.all()
    some_passcard = passcards[0]

    active_passcards = Passcard.objects.filter(is_active=True)

    print('Всего пропусков:', Passcard.objects.count())  # noqa: T001
    print("Активных пропусков:", len(active_passcards))
