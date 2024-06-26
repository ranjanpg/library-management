# Generated by Django 5.0.6 on 2024-06-19 17:53

from django.db import migrations, models

booksToUpdate = {}

def getBookUpdateData(apps, schema_editor):
    Book = apps.get_model('management', 'Book')
    for book in Book.objects.all():
        booksToUpdate[book.pk] = book.author_id

def updateBooks(apps, schema_editor):
    Book = apps.get_model('management', 'Book')
    Author = apps.get_model('management', 'Author')
    for book_id, author_id in booksToUpdate.items():
        book = Book.objects.get(pk=book_id)
        author = Author.objects.get(pk=author_id)
        book.authors.add(author)

class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_member_finesaccrued'),
    ]

    operations = [
        migrations.RunPython(getBookUpdateData, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='management.author'),
        ),
        migrations.RunPython(updateBooks, migrations.RunPython.noop),
    ]
