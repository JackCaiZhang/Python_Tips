from argparse import ArgumentParser
from rich_argparse import RichHelpFormatter
from datetime import datetime

def run_etl(date, city, dry_run, incremental):
    print(f'Running ETL for {city} on {date}...')
    print(f'Dry run: {dry_run}, Incremental: {incremental}')
    # your real ETL code here...

if __name__ == '__main__':
    parser = ArgumentParser(
        description='🔥 Run the ETL Pipeline with Beautiful Rich-Argparse Output.',
        formatter_class=RichHelpFormatter
    )

    parser.add_argument(
        '--date',
        default=datetime.today().strftime('%Y-%m-%d'),
        help='Specify which date to run. Defaults to today.'
    )
    parser.add_argument(
        '--city',
        required=True,
        help='City name, e.g. beijing / shanghai / guangzhou.'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Run validation without writing to database.'
    )
    parser.add_argument(
        '--incremental',
        action='store_true',
        help='Ingest only new or updated records.'
    )

args = parser.parse_args()
run_etl(args.date, args.city, args.dry_run, args.incremental)