def handle(response, expected_status_codes: list[int], ignored_status_codes=None):

    # Replacing mutable default argument
    if ignored_status_codes is None:
        ignored_status_codes = []

    if response.status_code in ignored_status_codes:
        print(f'Received status code {response.status_code}, but ignored.')
        return

    if response.status_code not in expected_status_codes:
        print(f'{response.status_code} {response.text}')
        exit(1)
