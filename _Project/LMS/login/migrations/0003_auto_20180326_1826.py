# Generated by Django 2.0.2 on 2018-03-26 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180326_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('connection_id', models.IntegerField(primary_key=True, serialize=False)),
                ('connection_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.LMSUser')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Course',
            fields=[
                ('student_course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacher_feedback', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Exercise',
            fields=[
                ('student_exercise_id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_attempts', models.IntegerField()),
                ('number_of_tries', models.FloatField()),
                ('time_spend_by_exercises', models.IntegerField()),
                ('time_spend_succeed', models.IntegerField()),
                ('total_time_spent', models.IntegerField()),
                ('number_abort', models.IntegerField()),
                ('score', models.FloatField()),
                ('number_correct_attempts', models.IntegerField()),
                ('student_level', models.CharField(max_length=2)),
                ('completed_time', models.IntegerField()),
                ('feedback', models.CharField(max_length=100)),
                ('submit_date', models.DateTimeField()),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Exercise')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.LMSUser')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Question',
            fields=[
                ('student_question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_status', models.IntegerField(choices=[('SK', 'Skipped'), ('CR', 'Correct'), ('IN', 'Incorrect'), ('ST', 'Started'), ('NL', 'Null')], default='NL', max_length=2, null=True)),
                ('time_spent', models.IntegerField()),
                ('submit_date', models.DateTimeField()),
                ('Question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Question')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.LMSUser')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Sheet',
            fields=[
                ('student_sheet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('feedback', models.CharField(max_length=100)),
                ('total_time_spent', models.IntegerField()),
                ('sheet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Sheet')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.LMSUser')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher_feedback',
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.LMSUser'),
        ),
        migrations.AddField(
            model_name='student_course',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Course'),
        ),
        migrations.AddField(
            model_name='student_course',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.LMSUser'),
        ),
    ]