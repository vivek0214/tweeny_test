## Team Deadpool

## Tweeny test one

## Tech/framework used

- **Python** (v3.7.x)
- **MongoDB** (v4.x)

## Installation

pip install -r requirements.txt

### MongoDB Setup

Create Database

    use mydb

Create DB User

    db.createUser(
        {
    	    user: "game_user",
    	    pwd: "######",
    	    roles: ["readWrite", "dbAdmin"]
    	}
    )

### Virtual Env Setup

    virtualenv -p python3.7 <env_name>

## API Reference
