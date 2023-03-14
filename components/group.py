import typer
import requests
from lib import api_response_handling


class Groups:

    def __init__(self, conf):
        self.conf = conf

    def get_app(self):
        app = typer.Typer(add_completion=False, help="Group related operations")

        @app.command()
        def create(
                group: str = typer.Argument(..., help="The name of the group"),
                description: str = typer.Argument(..., help="The description of the group"),
                active: bool = typer.Option(True, help="The group will be active/inactive on creation")
        ):
            """
            Creates <group> with <description>, that is <active> in all directories specified in the config.
            """
            for directory in self.conf['directories']:
                print(f"Adding {group} to directory: {directory['name']}")
                response = requests.post(
                    f"{self.conf['domain']}/rest/usermanagement/1/group",
                    json={"name": group, "description": description, "type": "GROUP", "active": active},
                    auth=(directory['username'], directory['password']),
                    headers={'Content-type': 'application/json'}
                )
                api_response_handling.handle(response, expected_status_codes=[201])

        @app.command()
        def delete(
                group: str = typer.Argument(..., help="The name of the group"),
                skip_missing_group_error: bool = typer.Option(False, "--ignore-if-missing/--exit-if-missing",
                                                              help="Ignore/exit if the group is missing")
        ):
            """
            Removes <group> from all directories specified in the config.
            """
            for directory in self.conf['directories']:
                print(f"Deleting {group} in directory: {directory['name']}")
                response = requests.delete(
                    f"{self.conf['domain']}/rest/usermanagement/1/group",
                    params={"groupname": group},
                    auth=(directory['username'], directory['password']),
                    headers={'Content-type': 'application/json'}
                )
                if skip_missing_group_error:
                    api_response_handling.handle(response, expected_status_codes=[204], ignored_status_codes=[404])
                else:
                    api_response_handling.handle(response, expected_status_codes=[204])

        @app.command()
        def add(
                parent_group: str = typer.Argument(..., help="The parent group"),
                child_group: str = typer.Argument(..., help="The child group")
        ):
            """
            Adds the <child_group> as a direct member to the <parent_group> in all directories specified in the config.
            """
            for directory in self.conf['directories']:
                print(f"Adding {child_group} to {parent_group} in directory: {directory['name']}")
                response = requests.post(
                    f"{self.conf['domain']}/rest/usermanagement/1/group/child-group/direct",
                    params={"groupname": parent_group},
                    json={"name": child_group},
                    auth=(directory['username'], directory['password']),
                    headers={'Content-type': 'application/json'}
                )
                api_response_handling.handle(response, expected_status_codes=[201])

        return app
