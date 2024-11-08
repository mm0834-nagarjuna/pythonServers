from hdbcli import dbapi
from DataBaseConnection import dbConnect

def execute_query(query):
    result = dbConnect()
    status = result['status']
    message = result['message']
    connection = result['connection']
    response = {'status': status, 'message': message}

    if status == 'success':
        cursor = connection.cursor()
        try:
            for command in query:
                if isinstance(command, str):
                        if  command.startswith('UPDATE' or 'DELETE'):
                            cursor.execute(command)
                            connection.commit()
                            response['dataMessage'] = "Query executed successfully"
                            response['query'] = query
                        elif  command.startswith('SELECT') :
                            cursor.execute(command)
                            columns = [desc[0] for desc in cursor.description]
                            results = cursor.fetchall()
                            rows = [dict(zip(columns, row)) for row in results]
                            response['data'] = rows
                            response['query'] = query
                        else :
                            response['error'] = 'Insert data is Not possible in this Application'
        except dbapi.Error as e:
            response['error'] = f"Error executing query: {e}"

        finally:
            cursor.close()
            connection.close()
    else:
        response['error'] = "Connection failed"
    return response
