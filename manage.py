'''
Author: duck 762202223@qq.com
Date: 2025-09-02 18:34:32
LastEditors: duck 762202223@qq.com
LastEditTime: 2025-09-03 10:29:37
FilePath: /new_django/manage.py
Descsyyiption: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%
'''
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from django.core.management.commands.runserver import Command as Runserver
import os
import sys




def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':  
    Runserver.default_addr = '127.0.0.1'
    Runserver.default_port = 8089
    main()
