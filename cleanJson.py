import json
import re
def parse_generate_response(response):
    
    try:
       
        raw_json_string = response.text
        print("raw_json_string->", raw_json_string)
        normalized_string = re.sub(r'\\\\+', r'\\', raw_json_string)
        
        
        cleaned_json_string = normalized_string.strip()
    


      
        sql_commands = json.loads(cleaned_json_string)

     
        return sql_commands
    except json.JSONDecodeError as e:

        return {'error': str(e)}

    except Exception as e:

        return {'error': str(e)}

