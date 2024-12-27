import os
import string
from django.utils.timezone import now
from django.db import models
import random

def image_path(instance, filename):
    user_id = instance.user.id 
    extension = filename.split('.')[-1]
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    new_filename = f"{now().strftime('%Y%m%d%H%M%S')}_{random_str}.{extension}"
    save_path = os.path.join('posts', str(user_id), 'post_images', new_filename)
    return save_path