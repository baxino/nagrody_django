# Generated by Django 5.0.1 on 2024-01-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nagrody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ_nagrody', models.CharField(choices=[('nagrody ministra', 'nagrody ministra właściwego do spraw oświaty i wychowania'), ('nagrody WKO', 'nagrody Wielkopolskiego Kuratora Oświaty')], max_length=50)),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=100)),
                ('data_ur', models.CharField(max_length=100)),
                ('miejsce_ur', models.CharField(max_length=100)),
                ('zajmowane_stanowisko', models.CharField(choices=[('dyrektor', 'dyrektor'), ('nauczyciel', 'nauczyciel (także wicedyrektor)')], max_length=70)),
                ('posiadane_wyksztalcenie', models.CharField(choices=[('srednie', 'średnie z przygotowaniem pedagogicznym'), ('srednie_zaklad', 'średnie z przygotowaniem pedagogicznym - Zakład kształcenia Nauczycieli'), ('wyzsze', 'wyższe zawodowe z przygotowaniem pedagogicznym')], max_length=70)),
            ],
        ),
    ]
