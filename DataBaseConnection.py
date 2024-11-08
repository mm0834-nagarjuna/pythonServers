from hdbcli import dbapi
import json

def dbConnect():
    try:
        file_path = 'Dbconfig.json'
        with open(file_path, 'r') as file:
            data = json.load(file)
        conn = dbapi.connect(
            address=data[0]['host'],
            port=data[0]['port'],
            user=data[0]['user'],
            password=data[0]['password']
        )
        return {
            'status': 'success',
            'message': 'Database connected successfully',
            'connection': conn
        }
    except Exception as e:
         return{
            'status': 'error',
            'message': f'Error during connection: {str(e)}',
            'connection': None
        }
    




