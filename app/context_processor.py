from notifications.models import Notification

def notifications(request):
    return {'notifications': Notification.objects.all()}