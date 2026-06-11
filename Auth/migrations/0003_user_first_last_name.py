from django.db import migrations, models


def split_full_name(apps, schema_editor):
    User = apps.get_model('Auth', 'User')
    for user in User.objects.all():
        full_name = (getattr(user, 'full_name', '') or '').strip()
        if full_name:
            first_name, _, last_name = full_name.partition(' ')
            user.first_name = first_name
            user.last_name = last_name
        user.save(update_fields=['first_name', 'last_name'])


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_emailotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.RunPython(split_full_name, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
