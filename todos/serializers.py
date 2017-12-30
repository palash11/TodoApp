from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Todo
        fields = ('url', 'id', 'taskName', 'createdAt', 'isDone', 'doneAt', 'user')
        extra_kwargs = {
            'url': {
                'view_name': 'todos:todo-detail',
            }
}
