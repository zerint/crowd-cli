import typer
import requests

JSON_HEADER = {'Content-type': 'application/json'}


class Groups:

    def __init__(self, conf):
        self.conf = conf

    def get_app(self):
        app = typer.Typer(add_completion=False)

        @app.command()
        def create(group: str, description: str, active: bool = True):
            for directory in self.conf['directories']:
                json_data = {
                    "name": group,
                    "description": description,
                    "type": "GROUP",
                    "active": active
                }
                print(f"Adding {group} to directory: {directory['name']}")
                x = requests.post(
                    f"{self.conf['domain']}/rest/usermanagement/1/group",
                    json=json_data,
                    auth=(directory['username'], directory['password']),
                    headers=JSON_HEADER
                )
                if x.status_code != 201:
                    print(x.status_code)
                    print(x.text)
                    exit(1)

        @app.command()
        def delete(group: str, skip_missing_group_error: bool = False):
            for directory in self.conf['directories']:
                print(f"Deleting {group} to directory: {directory['name']}")
                x = requests.delete(
                    f"{self.conf['domain']}/rest/usermanagement/1/group",
                    params={"groupname": group},
                    auth=(directory['username'], directory['password']),
                    headers=JSON_HEADER
                )
                if skip_missing_group_error and x.status_code == 404:
                    print('   Skipped missing group error, because of flag: skip_missing_group_error = True')
                    continue

                if x.status_code != 204:
                    print(x.status_code)
                    print(x.text)
                    exit(1)

        @app.command()
        def add(group: str, child_group: str):
            for directory in self.conf['directories']:
                print(f"Adding {child_group} to {group} in directory: {directory['name']}")
                x = requests.post(
                    f"{self.conf['domain']}/rest/usermanagement/1/group/child-group/direct",
                    params={"groupname": group},
                    json={"name": child_group},
                    auth=(directory['username'], directory['password']),
                    headers={'Content-type': 'application/json'}
                )
                if x.status_code != 201:
                    print(x.status_code)
                    print(x.text)
                    exit(1)

        return app
