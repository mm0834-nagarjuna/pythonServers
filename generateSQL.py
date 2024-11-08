import json
from cleanJson import parse_generate_response

def generateSQL(model,question):
    from Prompt import MY_BOOKSHOP_ACTUAL_ORDERS
    response = model.start_chat().send_message(f"{MY_BOOKSHOP_ACTUAL_ORDERS}\n{question}")
    try:
      # Send the message to the model
      sql_commands = parse_generate_response(response)
      sql_command = []
      if (sql_commands.get("SQL") or sql_commands.get("sql")):
        sql_command.append(sql_commands.get("SQL") or sql_commands.get("sql"))
      if (sql_commands.get("SQL1") and sql_commands.get("SQL1")):
        sql_command.append(sql_commands.get("SQL1"))
        sql_command.append(sql_commands.get("SQL2"))
      return sql_command
    except Exception as e:
      return ('error', e)