from ollama import Client

# Initialize Ollama client
def summarize(scene, objects_scene):
    client = Client()
    text = "Your name is Sarvam, rewrite this text,"
    text += scene
    text += " the objects in scene" + objects_scene
    text = text + "now include the objects in the scene and rewrite it."
    # Send a prompt to the model
    response = client.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': text
        }
    ])

    return response['message']['content']