import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduSense.settings')

django.setup()

# Import function
from learning.utils import import_markdown_topic


# ALL TOPICS LIST
topics = [

    {
        "subject_name": "Java",
        "subject_slug": "java",

        "unit_title": "Introduction & Basic Concept",
        "unit_slug": "unit1-introduction-basic-concept",

        "topic_title": "JDK JRE JVM",
        "topic_slug": "jdk-jre-jvm",

        "markdown_file_path":
        r"markdown_uploads\Java\unit1.Introduction and Basic Concept\JDK-JRE-JVM.md"
    },

    {
        "subject_name": "Java",
        "subject_slug": "java",

        "unit_title": "Introduction & Basic Concept",
        "unit_slug": "unit1-introduction-basic-concept",

        "topic_title": "Variables Datatype Operators",
        "topic_slug": "variables-datatype-operators",

        "markdown_file_path":
        r"markdown_uploads\Java\unit1.Introduction and Basic Concept\Variables_datatype_operators.md"
    }

]


# IMPORT LOOP
for topic in topics:

    try:

        result = import_markdown_topic(

            subject_name=topic["subject_name"],
            subject_slug=topic["subject_slug"],

            unit_title=topic["unit_title"],
            unit_slug=topic["unit_slug"],

            topic_title=topic["topic_title"],
            topic_slug=topic["topic_slug"],

            markdown_file_path=topic["markdown_file_path"]

        )

        print(f"SUCCESS: {result}")

    except Exception as e:

        print(f"ERROR: {e}")