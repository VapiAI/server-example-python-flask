import os
import json  # Add this line

from llama_index import VectorStoreIndex, SimpleDirectoryReader

data_path = os.path.abspath(os.path.join(os.getcwd(),"data"))

def get_character_inspiration(inspiration):
    fallbackResponse = {
        "result": "Sorry, I am dealing with a technical issue at the moment, perhaps because of heightened user traffic. Come back later and we can try this again. Apologies for that."
    }
    if inspiration:
        try:
            if os.path.exists(data_path):
                required_exts = [".md"]
                reader = SimpleDirectoryReader(
                    input_dir=data_path, 
                    required_exts=required_exts, 
                    recursive=True
                )
                documents = reader.load_data()
                index = VectorStoreIndex.from_documents(documents)

                queryEngine = index.as_query_engine()
                response = queryEngine.query(inspiration)

                # Convert response to a JSON-serializable data structure
                json_serializable_response = {
                    "result": response.result,
                    "score": response.score,
                    "data": response.data
                }

                return json_serializable_response  # Serialize the data to JSON
            else:
                return json.dumps(fallbackResponse)  # Serialize the fallback response to JSON
        except Exception as e:
            return (fallbackResponse)  # Serialize the fallback response to JSON
    else:
        return (fallbackResponse)  # Serialize the fallback response to JSON