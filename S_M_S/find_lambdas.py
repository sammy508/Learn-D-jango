import os
import importlib
import pkgutil
import inspect

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "S_M_S.settings")
django.setup()

package_name = "student_management_system"

package = importlib.import_module(package_name)

def find_lambdas(pkg):
    for loader, module_name, is_pkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        try:
            module = importlib.import_module(module_name)
        except Exception:
            continue
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and obj.__name__ == "<lambda>":
                print(f"Found lambda: {module_name}.{name}")
            if inspect.isclass(obj):
                for attr_name, attr_value in inspect.getmembers(obj):
                    if callable(attr_value) and getattr(attr_value, "__name__", None) == "<lambda>":
                        print(f"Found lambda in class: {module_name}.{obj.__name__}.{attr_name}")

find_lambdas(package)
