from users.models import Client , Agent

def create_user_by_type(backend, user, request ,  response, *args, **kwargs):


    if request['user_type'] == "client" and not Client.objects.filter(user_id=user.id):
        Client.objects.create(user_id=user.id)



    elif not Agent.objects.filter(user_id=user.id):
        Agent.objects.create(user_id=user.id)
