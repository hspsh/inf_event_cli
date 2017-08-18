# inf_events_cli

## Installation

0. Clone this repo:

```bash
    git clone https://github.com/hs3city/inf_event_cli
```

1. Enter folder:
```
    cd inf_event_cli
```

2. Create virtualenv:
```
    virtualenv -p python3 env
```

3. Activate virtualenv
```
    . env/bin/activate
```

4. Install requirements
```
    pip install -r requirements.txt
```

5. Add your Meetup API key
```
    python3 main.py auth [API Key]
```

## Usage

Providing that you have virtualenv activated

```
    python3 main.py add [Event_file.yml]
```

## Event file format

- YAML
- Must contain:
    - date
    - time
    - name
    - description
- May contain:
    - comments / message from event creator

Sample file is located in ```docs/sample_event_file.yml```
