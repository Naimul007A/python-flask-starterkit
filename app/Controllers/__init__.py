# Controllers package
import os
import importlib
from flask import Blueprint


def get_all_blueprints():
    """
    Automatically discover and return all blueprints from the Controllers package
    """
    blueprints = []

    # Get the current directory (Controllers folder)
    current_dir = os.path.dirname(__file__)

    # Iterate through all Python files in the Controllers directory
    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            # Get module name (remove .py extension)
            module_name = filename[:-3]

            try:
                # Import the module dynamically
                module = importlib.import_module(f"app.Controllers.{module_name}")

                # Look for blueprint objects (variables ending with '_bp')
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, Blueprint) and attr_name.endswith("_bp"):
                        blueprints.append(attr)
                        print(
                            f"✓ Auto-discovered blueprint: {attr_name} from {module_name}"
                        )

            except Exception as e:
                print(f"⚠ Error importing {module_name}: {e}")

    return blueprints


def register_all_blueprints(app):
    """
    Automatically register all discovered blueprints with the Flask app
    """
    blueprints = get_all_blueprints()

    for blueprint in blueprints:
        app.register_blueprint(blueprint, url_prefix="/api/v1")
        print(f"✓ Registered blueprint: {blueprint.name}")

    print(f"🎉 Total blueprints registered: {len(blueprints)}")
    return len(blueprints)
