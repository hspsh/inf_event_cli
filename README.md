# inf_events_cli

## Installation

0. Clone this repo:

  ```bash
    git clone https://github.com/hs3city/inf_event_cli
  ```

1. Enter folder:

  ```bash
    cd inf_event_cli
  ```

2. Create virtualenv:

  ```bash
    virtualenv -p python3 venv
  ```

3. Activate virtualenv

  ```bash
    . venv/bin/activate
  ```

4. Install requirements

  ```bash
    pip install -r requirements.txt
  ```

5. Add your Meetup API key

  ```bash
    python3 main.py auth [API Key]
  ```

You can obtain your API key [here](https://secure.meetup.com/meetup_api/key/)

## Usage

Providing that you have virtualenv activated

```bash
  python3 main.py add [Event_file.yml]
```

## Event file format

- YAML
- Must contain:

  - date
  - time
  - name (**CAUTION** Be sure to wrap in quotes)
  - description (**CAUTION** Be sure to wrap in quotes)

- May contain:

  - comments / message from event creator

Sample file is located in ```docs/sample_event_file.yml```
