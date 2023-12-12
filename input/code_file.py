import argparse
from db import init_db, load_db_schema, build_insert, insert_into_db, is_unused_id, update_column
from sqlite3 import connect, Cursor



def main():
    parser = argparse.ArgumentParser(description="A sample project for joining players to tables.")
    subparsers = parser.add_subparsers(dest="command")

    # join command
    join_parser = subparsers.add_parser('join', help='Join a player to a table.')

    join_parser.add_argument('--table', required=True, help='The name of the table.')
    join_parser.add_argument('--player', required=True, help='The name of the player.')

    # add other commands here

    # init command
    init_parser = subparsers.add_parser('init', help='Initialize the game database.')
    init_parser.add_argument('--dbname', default='poker.db', help='The name of the database file.')


   # general
    args = parser.parse_args()

    match args.command:
        case 'join':
            response: str = join(args.table, args.player)
        case 'init':
            response: str = init_db(args.dbname)
        case _:
            parser.print_help()
            return
    
    print(response)


def join(table_name: str, player_name: str) -> None: 
    tables: dict = load_db_schema('db_schema.json')
    is_active: int = 0
    is_queued: int = 1

    if is_unused_id(table_name='players', id=player_name):
        insert_into_db(build_insert({'players': tables['players']}, [player_name, table_name, is_queued]))

    if is_unused_id(table_name='tables', id=table_name):
        insert_into_db(build_insert({'tables': tables['tables']}, [table_name, is_active]))
    else:
        update_column(table_name='tables', column_name='active', value=1)
        update_column(table_name='players', column_name='queued', value=0)

    return True



if __name__ == '__main__': 
    main()