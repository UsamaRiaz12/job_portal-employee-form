# Generated by Django 4.1.5 on 2023-08-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("em_register", "0004_em_register_name2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="em_register",
            name="degree",
        ),
        migrations.RemoveField(
            model_name="em_register",
            name="name2",
        ),
        migrations.AddField(
            model_name="em_register",
            name="city",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.AddField(
            model_name="em_register",
            name="number",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="email",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="name",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="em_register",
            name="resume",
            field=models.FileField(default="", upload_to="resumes/"),
        ),
    ]
