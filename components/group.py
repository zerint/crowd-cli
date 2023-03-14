import typer
import requests
from lib import api_response_handling


class Groups:

    def __init__(self, conf):
        self.conf = conf

    def get_app(self):
        app = typer.Typer(add_completion=False)

        @app.command()
        def create(group: str, description: str, active: bool = True):
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
        def delete(group: str, skip_missing_group_error: bool = False):
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
        def add(group: str, child_group: str):
            for directory in self.conf['directories']:
                print(f"Adding {child_group} to {group} in directory: {directory['name']}")
                response = requests.post(
                    f"{self.conf['domain']}/rest/usermanagement/1/group/child-group/direct",
                    params={"groupname": group},
                    json={"name": child_group},
                    auth=(directory['username'], directory['password']),
                    headers={'Content-type': 'application/json'}
                )
                api_response_handling.handle(response, expected_status_codes=[201])

        return app
