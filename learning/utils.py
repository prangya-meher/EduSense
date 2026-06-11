from .models import (
    Subject,
    Unit,
    Topic
)


def import_markdown_topic(

    subject_name,
    subject_slug,

    unit_title,
    unit_slug,

    topic_title,
    topic_slug,

    markdown_file_path
):

    with open(
        markdown_file_path,
        'r',
        encoding='utf-8'
    ) as file:

        markdown_content = file.read()


    subject, created = Subject.objects.get_or_create(

        slug=subject_slug,

        defaults={

            'name': subject_name
        }
    )


    unit, created = Unit.objects.get_or_create(

        slug=unit_slug,

        defaults={

            'subject': subject,
            'title': unit_title
        }
    )


    topic, created = Topic.objects.get_or_create(

        slug=topic_slug,

        defaults={

            'unit': unit,
            'title': topic_title,
            'markdown_content': markdown_content
        }
    )


    if not created:

        topic.markdown_content = markdown_content

        topic.save()


    return topic