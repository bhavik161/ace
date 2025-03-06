import psycopg2
from aws_secrets import get_secret
from config import REDSHIFT_HOST, REDSHIFT_PORT, REDSHIFT_DBNAME

def create_loan_profile(sql_statement):
    """Executes the SQL statement in Redshift and returns the row count."""
    credentials = get_secret()
    if not credentials:
        raise ValueError("Failed to retrieve Redshift credentials.")
    
    REDSHIFT_USER = credentials["username"]
    REDSHIFT_PASSWORD = credentials["password"]

    try:
        conn = psycopg2.connect(
            dbname=REDSHIFT_DBNAME,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD,
            host=REDSHIFT_HOST,
            port=REDSHIFT_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(sql_statement)
        cur.execute("SELECT COUNT(*) FROM lp.new_loan_profile;")
        count = cur.fetchone()[0]

        cur.close()
        conn.close()
        return count

    except Exception as e:
        return f"Error executing SQL: {e}"
